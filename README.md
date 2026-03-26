# Tesi

# Gestione dell’ambiente di sviluppo e configurazione del repository

All’interno del progetto è stata creata la cartella dataset/, nella quale sono stati caricati diversi file JSON di grandi dimensioni necessari per le analisi. Tuttavia, tali file superavano il limite massimo consentito da GitHub (100 MB per singolo file).

# Download file Json

Poiché i file JSON contenuti nella cartella dataset/ superano il limite massimo di 100 MB imposto da GitHub, è stato deciso di non includerli direttamente nel repository, ma di renderli disponibili tramite link esterni. In questo modo è possibile mantenere leggero il repository garantendo comunque l’accesso ai dati necessari per l’esecuzione del progetto.

I dataset possono essere scaricati dai seguenti link:

- australian_user_reviews.json: https://mcauleylab.ucsd.edu/public_datasets/data/steam/australian_user_reviews.json.gz

- australian_users_items.json: https://mcauleylab.ucsd.edu/public_datasets/data/steam/australian_users_items.json.gz

- steam_games.json: https://cseweb.ucsd.edu/~wckang/steam_games.json.gz

Questi file devono essere posizionati all’interno della cartella dataset/ per poter essere utilizzati correttamente dagli script del progetto.

