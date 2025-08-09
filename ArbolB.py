class NodoB:
    def __init__(self, es_hoja=True):
        self.orden = 5
        self.claves = []         
        self.hijos = []          
        self.es_hoja = es_hoja 


class ArbolB:
    def nodo_lleno(self, nodo):
        return len(nodo.claves) >= 4

    def insertar_en_hoja(self, nodo, clave):
        for c in nodo.claves:
            if c.Id == clave.Id:
                return  
        nodo.claves.append(clave)
        nodo.claves.sort(key=lambda e: e.Id)

    def buscar_hijo_para_clave(self, nodo, clave):
        for i, k in enumerate(nodo.claves):
            if clave.Id < k.Id:
                return i
        return len(nodo.claves)

    def insertar(self, nodo, clave):
        if nodo.es_hoja:
            self.insertar_en_hoja(nodo, clave)
        else:
            i = self.buscar_hijo_para_clave(nodo, clave)
            hijo = nodo.hijos[i]
            self.insertar(hijo, clave)

    def dividir_nodo(self, nodo):
        imedio = 2
        clavemedia = nodo.claves[imedio]

        nodo_izq = NodoB(nodo.es_hoja)
        nodo_der = NodoB(nodo.es_hoja)

        nodo_izq.claves = nodo.claves[:imedio]
        nodo_der.claves = nodo.claves[imedio + 1:]

        if not nodo.es_hoja:
            nodo_izq.hijos = nodo.hijos[:imedio + 1]
            nodo_der.hijos = nodo.hijos[imedio + 1:]

        return clavemedia, nodo_izq, nodo_der

    def insertary_dividir(self, nodo, clave):
        if nodo.es_hoja:
            self.insertar_en_hoja(nodo, clave)
        else:
            indice = self.buscar_hijo_para_clave(nodo, clave)
            hijo = nodo.hijos[indice]
            resultado = self.insertary_dividir(hijo, clave)

            if resultado is not None:
                clavemedia, nodo_izq, nodo_der = resultado
                nodo.claves.insert(indice, clavemedia)
                nodo.hijos[indice] = nodo_izq
                nodo.hijos.insert(indice + 1, nodo_der)

        if self.nodo_lleno(nodo):
            return self.dividir_nodo(nodo)
        else:
            return None
        
    def crear_nueva_raiz(self, clave_media, nodo_izquierdo, nodo_derecho):
        nueva_raiz = NodoB(es_hoja=False)
        nueva_raiz.claves = [clave_media]
        nueva_raiz.hijos = [nodo_izquierdo, nodo_derecho]
        return nueva_raiz

    def insertar_en_arbol(self, raiz, clave):
        resultado = self.insertary_dividir(raiz, clave)
        if resultado is not None:
            clave_media, nuevo_izq, nuevo_der = resultado
            raiz = self.crear_nueva_raiz(clave_media, nuevo_izq, nuevo_der)
        return raiz

    def recorrido_inorden(self, nodo):
        for i in range(len(nodo.claves)):
            if not nodo.es_hoja:
                self.recorrido_inorden(nodo.hijos[i])
            nodo.claves[i].ImprimirporCalificacion()
        if not nodo.es_hoja:
            self.recorrido_inorden(nodo.hijos[-1])


            