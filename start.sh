if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/sajalkmr/JonasDarkBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /JonasDarkBot
fi
cd /JonasBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py