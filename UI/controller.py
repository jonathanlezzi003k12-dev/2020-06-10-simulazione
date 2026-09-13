
import flet as ft
class Controller:

    def __init__(self,view, model):
        self._view=view
        self._model=model
        self._genere=None
        self._attore=None
        self._ngiorni=None




    def hendlecreagrafo(self,e):
        #devo  gestire i casi in cui l'utente non inserisca niente
        if self._genere is None:
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text("Attenzione non hai inserito il genere",color="red"))
            self._view.update_page()
            return
        #carico grafo
        self._model.loadgraph()
        self._view.lst_result.controls.clear()
        archi=len(self._model.returnArchi())
        nodi=len(self._model.returnNodi())
        self._view.lst_result.controls.append(ft.Text(f"Grafo generato correttamente con vertici {nodi} e archi {archi}",color="green"))
        self._view.ddAttore.disabled=False
        self._view.txtFielfGiorni.disabled=False
        #qui riempio il secondo dropp down
        self.riempiddAttori(self._view.ddAttore)

        self._view.update_page()





    def riempiddGenere(self,dd):
        generi=self._model.getGeneriFromDao()
        for g in generi:
           dd.options.append(ft.dropdown.Option(text=g,
                                                data=g,
                                                on_click=self.assegnaGenere))

    def assegnaGenere(self,e):
        self._genere=e.control.data
        self._model.scegliGenere(self._genere)

#=================================================================
#=================================================================
    #prova
    def riempiddGenere2(self,dd):
        generi=self._model.getGeneriFromDao()
        for g in generi:
           dd.options.append(ft.dropdown.Option(text=g))


    def assegnaGenere2(self,e):
        self._genere=e.control.value
        self._model.scegliGenere(self._genere)

#=================================================================
#=================================================================

    def riempiddAttori(self,ddattori):
        attori=self._model.attoriGrafo()
        for at in attori:
            ddattori.options.append(ft.dropdown.Option(text=at.first_name,
                                                       data=at,
                                                       on_click=self.assegnaAttore))


    def assegnaAttore(self,e):
        self._attore=e.control.data
        self._model.attoreScelto(self._attore)


    def hendleAttoriSimili(self,e):

        if self._attore is None:
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text("non hai inserito l'attore", color="red"))
            self._view.update_page()
            return

        attoriRaggiungibili=self._model.attoriRaggingibiliDaAttoreDato(self._attore)
        for a in attoriRaggiungibili:
            self._view.lst_result.controls.append(ft.Text(f"gli attori simili sono{a.first_name}", color="green"))
        self._view.update_page()

    def simulazione(self):
        giorni=int(self._view._txtFielfGiorni.value)

        if giorni=="":
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text("non hai inserito il giorno", color="red"))
            self._view.update_page()

        try:
            g=int(giorni)
        except ValueError:
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text("il giorno non è un numero", color="red"))
            self._view.update_page()

            return

        #ora model






