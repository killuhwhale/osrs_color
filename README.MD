# Socks Servers on GCP




## VENV/ Project setup
setup_project.py


## SSH with gloud client to remote linux server 
gcloud compute ssh --zone "us-central1-f" "osrs-socks-template-1"  --project "osrs-352704"

## Connect to Pi
    ssh pi@192.168.0.139

## Copy files to pi
    scp google_compute_engine  pi@192.168.0.139:~/.ssh

## Connect Device to Proxy SSH Tunnel
    ssh -D 13377  chrisandaya@34.121.188.5 -i ~/.ssh/google_compute_engine

## Start RuneLite w/ connection to proxy
    java -DsocksProxyHost=127.0.0.1 -DsocksProxyPort=13377 -jar runelite.jar





# Recipies
An entry(dict) in a dict, with two keys: fns & sleeps
    - fns: a list of function to be called one after the other in an infinite loop
    - sleeps


# Cookbook
    A group of recipies.
        - A list of recipes for each client.
    The idea is to be able to preconfigure a set of recipes for the clients to run on a given day.
    We can write out which client should execute which recipie.
    Then we can write many different cookbooks.
    When we run the bot, we choose a cookbook to run.


# Search for Images

Place needle image under:
    - needles/{recipe_name}/img_name.png


# Possible RuneLite Plugins
- onRunChanged....