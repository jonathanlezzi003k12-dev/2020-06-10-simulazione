import flet as ft

class View:
    def __init__(self,page:ft.Page):
        super().__init__()
        self._page=page
        self._controller=None
        #======================================================
        #======================================================
        #titolo
        self._title=None
        self._page.horizontal_alignment="CENTER"
        self._page.theme_mode = ft.ThemeMode.LIGHT
        page.window_width = 120
        page.window_height = 800
        page.window_center()

        #======================================================
        #======================================================
        #prima riga

        self._txtGenere=None
        self.ddGenere=None
        self._btnCreaGrafo=None


        #======================================================
        #======================================================
        #seconda riga

        self._txtAttore=None
        self.ddAttore=None
        self._btnAttoriSimili=None

        #======================================================
        #======================================================ù
        #terza riga
        self._txtGiorni=None
        self.txtFielfGiorni=None
        self._btnSimulazione=None
        self.lst_result=None



    def load_interface(self):
        #======================================================
        #titolo
        self._title=ft.Text("Simulazione del 2020" , color="blue")
        self._page.controls.append(self._title)


        #======================================================
        #prima riga
        self._txtGenere=ft.Text("Genere", color ="darkblue")
        self.ddGenere=ft.Dropdown(label="Genere",on_change=self._controller.assegnaGenere2)
        self._btnCreaGrafo=ft.ElevatedButton(text="crea grafo", on_click=self._controller.hendlecreagrafo)

        #self._controller.riempiddGenere(self.ddGenere)
        self._controller.riempiddGenere2(self.ddGenere)

        row1=ft.Row([ft.Container(self._txtGenere,width=300),
                     ft.Container(self.ddGenere,width=300),
                     ft.Container(self._btnCreaGrafo,width=300)],
                    alignment=ft.MainAxisAlignment.CENTER)




        #======================================================
        #seconda riga
        self._txtAttore=ft.Text("Attori", color ="darkblue")
        self.ddAttore=ft.Dropdown(label="Attore",disabled=True)
        self._btnAttoriSimili=ft.ElevatedButton(text="attori simili", on_click=self._controller.hendleAttoriSimili)




        row2=ft.Row([ft.Container(self._txtAttore,width=300),
                     ft.Container(self.ddAttore,width=300),
                     ft.Container(self._btnAttoriSimili,width=300)],
                    alignment=ft.MainAxisAlignment.CENTER)


        #======================================================
        #terza riga
        self._txtGiorni=ft.Text(value="giorni")
        self.txtFielfGiorni=ft.TextField(label="giorni", disabled=True)
        self._btnSimulazione=ft.ElevatedButton(text="Simulazione",on_click=self._controller.simulazione, color="green")



        row3=ft.Row([ft.Container(self._txtGiorni,width=300),
                     ft.Container(self.txtFielfGiorni,width=300),
                     ft.Container(self._btnSimulazione,width=300)],
                    alignment=ft.MainAxisAlignment.CENTER)

        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)
        self._page.controls.append(self.lst_result)
        self.update_page()

    def set_controller(self,controller):#costruttore
        self._controller=controller

    def update_page(self):
        self._page.update()



