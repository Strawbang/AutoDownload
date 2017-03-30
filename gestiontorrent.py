# -*- coding: utf-8 -*-
import transmissionrpc
import time
import sys
import datetime
reload(sys) # Reload does the trick!
sys.setdefaultencoding('UTF8')
#On part du principe que vous utilisez les ports de base pour votre transmission et on utilise le port habituel 9091.
tc = transmissionrpc.Client('localhost', port=9091, user='admin', password='')

#On récupére la date actuelle
datenow = datetime.datetime.now()
today2heure = now.replace(hour=2, minute=0, second=0, microsecond=0)
today7heure = now.replace(hour=7, minute=0, second=0, microsecond=0)
#On affiche tous les torrents en cours.
print tc.get_torrents()
print 'il y a: ',len(tc.get_torrents()),' torrents dans la liste'
#Pour chaque torrent en cours on va faire une serie de vérifications.
for torrent in tc.get_torrents() :
	if datenow > today2heure :
		tc.start_torrent(torrent.id,True)
	if datenow > today7heure :
		tc.stop_torrent(torrent.id,True)