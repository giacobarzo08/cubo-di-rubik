# EMULATORE DI UN CUBO RI RUBIK
Questo programma ha lo scopo di consentire all'utente di utilizzare un cubo di Rubik digitale: su un display vengono visualizzate tutte le facce del cubo ed è possibile ruotare il cubo nel modi standard, che sono spiegati poco sotto, come si farebbe con un cobo reale.
E' anche possibile, grazie alle funzioni della libreria `pyvista`, avere una vista cartesiana in 3D del cubo (è possibile anche, con una leggera modifica al codice: bisogna inserire il parametro `True` alla chimata della funzione `plt.plot_cube()` alla riga 182 del file `app.py`, passare ad una vista isometrica).

## Possibili Mosse
|Mossa |Rispettivo nel cubo |
|:----------: |:----------: |
|U |Gira il lato sopra in senso orario|
|U'|Gira il lato sopra in senso antiorario|
|F|Gira il lato frontale in senso orario|
|F'|Gira il lato frontale in senso antiorario|
|R|Gira il lato a destra in senso orario|
|R'|Gira il lato a destra in senso antiorario|
|L|Gira il lato a sinista in senso orario|
|L'|Gira il lato a sinista in senso antiorario|
|B|Gira il lato a dietro in senso orario|
|B'|Gira il lato a dietro in senso antiorario|
|D|Gira il lato sotto in senso orario|
|D'|Gira il lato sotto in senso antiorario|

## Installazione dei requisiti
Per utilizzare il programma è necessario Python 3, che è installabile in Windows direttamente da MS Store o in Linux tramite `apt`:
```bash
sudo apt update
sudo apt install python3 python3-pip pyton3-venv
```
OLtre alla librerie di sistema, è necessario installare la librerie `pyvista`. E' possibile farlo tramite l'installer di pacchetti Python `pip`:
```bash
pip install pyvista
```
In Ubuntu 24+ è necessrio usare un ambiente virtuale creato con `venv` per poter usare `pip`:
```bash
python3 -m venv name
source name/bin/activate

# eseguire tutti i comanti nell'ambiente

deactivate  # per uscire dall'ambiente
```
## Clonaggio del reperstory
E' possibile conare il reperstory con git tramite i protocolli `ssh` e `http`:
```bash
git clone git@github.com:giacobarzo08/cubo-di-rubik.git

# oppure

git clone http://github.com/giacobarzo08/cubo-di-rubik.git
```
E' necessario installare git nel caso non lo fosse già.
Installazione dal terminale (PowerShell o cmd) di windows:
```bash
winget install git
# riavviare il computer
```
Installazione su Linux:
```bash
sudo apt update
sudo apt install git zip unzip
# riavviare il computer/WSL
```
