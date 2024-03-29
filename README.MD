This is a multibox color bot. Which means to say, this bot is capable of running a color detection based script
on multiple clients at once on a single machine/cpu.

![osrs color sample](sample.gif)


The user can easily write steps to execute such as:

    def click_gilinor_guide(client, space=Spaces.PLAYER_CENTER_LG, chat_head_left=True):
        ''' Starting from somewhere in 1st house, lookfor 'FFFF0000' and click him 

        NPC Indicators
        '''
        if Search.chat_head_showing(client):
            return

        pt = Search.search_space_color(
            client, space, Colors.NPC_PURPLE)
        Search.click(pt)

        sleep(3)

        while not Search.chat_head_showing(client, left=chat_head_left):
            pt = Search.search_space_color(
                client, space, Colors.NPC_PURPLE)
            Search.click(pt)
            sleep(gauss(3, 0.5))


This will click on an NPC colored purple. If a misclick happens it will contiue to click on the NPC while the chat head is not showing.

Below is an explanation of how to write a script for this bot.



## VENV/ Project setup
setup_project.py

## SSH with gloud client to remote linux server 
gcloud compute ssh --zone "us-central1-f" "osrs-socks-template-1"  --project "osrs-352704"

## Connect to Pi
    ssh pi@192.168.0.139

## Copy files to pi so it can connect to GCP server
    scp google_compute_engine  pi@192.168.0.139:~/.ssh

## Create Device/ Pi SSH Tunnel
    ssh -D 13377  chrisandaya@34.121.188.5 -i ~/.ssh/google_compute_engine

## Start RuneLite w/ connection to proxy
    java -DsocksProxyHost=127.0.0.1 -DsocksProxyPort=13377 -jar runelite.jar


# Cookbook
A group of meals.
    - A list of meals, one for each client.

The idea is to be able to preconfigure a set of meals for the clients to run on a given day.
We can write out which client should execute which meal.
Then we can write many different cookbooks.
When we run the bot, we choose a cookbook to run.

# Meals
A meal is a list of recipies that the bot loop will execute for each client.

# Recipies
A recipie is a class that defines methods beginning with _r_, _s_, _v_ which define a single step, collectively.
A single step is composed of a recipie step, sleep, and verficiation.
These should be small tasks.


Each time the loop executes, the base task recipie will check the sleep(_s_) and verification (_v_) methods.
The _s_ method of the step will return an float which defines the amount of time to wait
before running the next recipie step.
The _v_ method of the step will return True, False or None. When returning True, the recipie is considered validated and will continue to next step.
If False, the _v_ will be called again on the next cycle.
If None, this will signal to the meal class, that this recipie is done and the next one should be ran.



# Search for Images
Place needle image under:
    - needles/{recipe_name}/img_name.png
    - needles/items/{item_enum_name}.png
    - needles/spaces/{space_enum_name}.png

# Possible RuneLite Plugins
- onRunChanged....