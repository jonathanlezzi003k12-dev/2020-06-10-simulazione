import copy

from database.DAO import DAO
import networkx as nx
import random


class Model:
    def __init__(self):

        #====================================
        #creo grafo

        self._graph=nx.Graph()

        #====================================
        # creo un id map
        self._idMapAttori={}
        attori=DAO.getAttori()
        for a in attori:
            self._idMapAttori[a.id]=a
        #====================================
        self._genere=None
        self._attoreScelto=None
        self._attori_delGenere=self._graph.nodes()




    def loadgraph(self):
        self._graph.add_nodes_from(self.getNodi(self._genere))
        self._getArchi()

    def getGeneriFromDao(self):
        generi=DAO.getGeneri()
        return generi

    def scegliGenere(self,genere):
        self._genere=genere

    def getNodi(self,genere):
        return DAO.getAttoriByGender(self._idMapAttori,genere)

    def returnArchi(self):
        return self._graph.edges()
    def returnNodi(self):
        return self._graph.nodes()

    def _getArchi(self):
        archi=  DAO.getArchiPesati(self._idMapAttori,self._genere)
        for a in archi:
            self._graph.add_edge(a[0],a[1],weight=a[2])



    def getAttori(self):
        return self._idMapAttori

    #def tipo_della_variabile_genere(self):
        #return type(self._genere)

    def returnArchi(self):
        return self._graph.edges


    #punto d
    def attoriGrafo(self):
        return self._graph.nodes

    def attoreScelto(self,attore):
        self._attoreScelto=attore

    #====================================================================================
    #====================================================================================
    #PUNTO D
    #esplorazione dei vertici a cui si può arrivare usando la componente connessa

    def attoriRaggingibiliDaAttoreDato(self,attore):
        lstComponenteConnessa=nx.node_connected_component(self._graph,attore)
        return sorted(lstComponenteConnessa,key=lambda a:a.last_name)



    #====================================================================================


    #utilizzo esplorazione del grafo per ampiezza
    def  attoriRaggingibiliDaAttoreDato2(self,attore):
        if attore not in self._graph:
            return []
        archiEsplorazioneAmpiezza=nx.bfs_edges(self._graph,attore)
        soluzione={attore}
        for u, v in archiEsplorazioneAmpiezza:
            soluzione.add(v)
        soluzione.discard(attore)
        return sorted(soluzione,key=lambda a:a.last_name)


    #====================================================================================
    #====================================================================================
    #INTERVISTA ATTORI
    #provo prima in maniera iterattiva e poi con ricorsione con ricorsione
    #da aggiustare


    def intervista(self,giorno):
        attori=list(self._attori_delGenere)
        result={}
        for g in range(1,giorno+1):
            if g==1:
                att=random.choice(attori)
                result[g]=att
                attori.remove(att)

            else:
                #============================================
                #condizione sul genere
                if g>=3:
                    if result[g-1].gender == result[g-2].gender and result[g-1].gender is not None :
                        if random.random()<0.90:
                            result[g]  =None
                #============================================
                #condizione di riempimento
                if result.get(g) is None and random.random() < 0.6 :
                    att=random.choice(attori)
                    result[g]=att
                    attori.remove(att)
                else:
                    listaDiViciniAttore=self.getViciniPesoMassimo(result[g])
                    if len(listaDiViciniAttore)==0:
                        att=random.choice(attori)
                        result[g]=att
                        attori.remove(att)
                    else:

                        #devo escludere tutti quelli a cui ho fatto l'intervista tra i vicini dell'attore precedentemente intervisatto
                        listaTemporanea=[]
                        for vic in listaDiViciniAttore:
                            if vic in result.keys():
                                listaDiViciniAttore.pop(vic)
                            else:
                                listaTemporanea.append(vic)
                        if len(listaTemporanea)==0:

                            att=random.choice(attori)
                            result[g]=att
                            attori.remove(att)
                        else:
                            att=random.choice(listaTemporanea)
                            result[g]=att
                            attori.remove(att)

                #===============================================
                #===============================================
                #condizione riempimento dopo la pausa

                if result[g-1] is None:
                    att=random.choice(self._attori_delGenere)
                    result[g]=att
                    attori.remove(att)

        return result


    def getViciniPesoMassimo(self,attore):
        lista={}
        valoreMassimo=-99999999
        listaVicini=list(self._graph.neighbors(attore))
        for v in listaVicini:
            if valoreMassimo<self._graph[attore][v]["weight"]:
                valoreMassimo=self._graph[attore][v]["weight"]
                lista.clear()
                lista[v]=valoreMassimo

            if valoreMassimo==self._graph[attore][v]["weight"]:
                lista[v]=valoreMassimo


        return list(lista.keys())


    #==================================================================






