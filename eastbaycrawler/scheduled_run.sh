# An example of how to run this using just cron.daily and at.

bot_script_location=~/python_fun/eastbaycrawler/run_bot.sh

# First run
timediff1="5 hours"
at now +`echo ${timediff1}` -f ${bot_script_location}

# Second run
timediff2="5 hours"
at now +`echo ${timediff2}` -f ${bot_script_location}