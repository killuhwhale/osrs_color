/*



runelite-client src main java net runelite client plugins aaaaappp



 * Copyright (c) 2019 Hydrox6 <ikada@protonmail.ch>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this
 *    list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
package net.runelite.client.plugins.aaaapp;

import net.runelite.api.*;
import net.runelite.api.events.ItemContainerChanged;
import net.runelite.client.callback.ClientThread;
import net.runelite.client.eventbus.Subscribe;
import net.runelite.client.game.ItemManager;
import net.runelite.client.plugins.Plugin;
import net.runelite.client.plugins.PluginDescriptor;
import net.runelite.client.ui.overlay.infobox.InfoBoxManager;

import okhttp3.*;

import javax.imageio.ImageIO;
import javax.inject.Inject;
import javax.swing.*;
import java.awt.image.BufferedImage;
import java.io.IOException;



@PluginDescriptor(
	name = "Aaaaappp",
	description = "Shows some stuff.",
	tags = {"app", "darts", "chinchompa", "equipment"}
)
public class CustomAmmoPlugin extends Plugin
{
	@Inject
	private Client client;

	@Inject
	private ClientThread clientThread;

	@Inject
	private InfoBoxManager infoBoxManager;

	@Inject
	private ItemManager itemManager;

	private CustomAmmoCounter counterBox;

	private final OkHttpClient okHttpClient = new OkHttpClient();

	@Override
	protected void startUp() throws Exception
	{

		clientThread.invokeLater(() ->
		{
			final ItemContainer container = client.getItemContainer(InventoryID.EQUIPMENT);

			try
			{
				System.out.println("Calliung Whoer.net");
				Request request = new Request.Builder()
						.url("https://whoer.net/")
						.build();

				okHttpClient.newCall(request).enqueue(new Callback()
				{
					@Override
					public void onFailure(Call call, IOException e)
					{
						System.out.println(e);
					}

					@Override
					public void onResponse(Call call, Response response) throws IOException
					{
						try (ResponseBody responseBody = response.body())
						{
							if (!response.isSuccessful())
							{
								System.out.println("Failed to download image ");
								return;
							}

							System.out.println(responseBody.source());



						}
					}
				});
			}
			catch (IllegalArgumentException | NullPointerException e)
			{
				System.out.println(e);
			}

			if (container != null)
			{
				checkInventory(container.getItems());
			}
		});
	}

	@Override
	protected void shutDown() throws Exception
	{
		infoBoxManager.removeInfoBox(counterBox);
		counterBox = null;
	}



	@Subscribe
	public void onChange(){

	}


	@Subscribe
	public void onItemContainerChanged(ItemContainerChanged event)
	{
		if (event.getItemContainer() != client.getItemContainer(InventoryID.EQUIPMENT))
		{
			return;
		}

		checkInventory(event.getItemContainer().getItems());
	}

	private void checkInventory(final Item[] items)
	{
		// Check for weapon slot items. This overrides the ammo slot,
		// as the player will use the thrown weapon (eg. chinchompas, knives, darts)
		if (items.length > EquipmentInventorySlot.WEAPON.getSlotIdx())
		{
			final Item weapon = items[EquipmentInventorySlot.WEAPON.getSlotIdx()];
			final ItemComposition weaponComp = itemManager.getItemComposition(weapon.getId());
			if (weaponComp.isStackable())
			{
				updateInfobox(weapon, weaponComp);
				return;
			}
		}

		if (items.length <= EquipmentInventorySlot.AMMO.getSlotIdx())
		{
			removeInfobox();
			return;
		}

		final Item ammo = items[EquipmentInventorySlot.AMMO.getSlotIdx()];
		final ItemComposition comp = itemManager.getItemComposition(ammo.getId());

		if (!comp.isStackable())
		{
			removeInfobox();
			return;
		}

		updateInfobox(ammo, comp);
	}

	private void updateInfobox(final Item item, final ItemComposition comp)
	{
		if (counterBox != null && counterBox.getItemID() == item.getId())
		{
			counterBox.setCount(item.getQuantity());
			return;
		}

		removeInfobox();
		final BufferedImage image = itemManager.getImage(item.getId(), 5, false);
		counterBox = new CustomAmmoCounter(this, item.getId(), item.getQuantity(), comp.getName(), image);
		infoBoxManager.addInfoBox(counterBox);
	}

	private void removeInfobox()
	{
		infoBoxManager.removeInfoBox(counterBox);
		counterBox = null;
	}
}
