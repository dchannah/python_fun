# An example of how to run this using just cron.daily and at.

bot_script_location=~/python_fun/eastbaycrawler/run_bot.sh
timediff="8 hours"
at now +`echo ${timediff}` -f ${bot_script_location}