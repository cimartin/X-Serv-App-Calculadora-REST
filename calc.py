import webapp
import csv


class calc (webapp.webApp):
    

    
    op1 = 0
    op2 = 0
    operacion = ''

    def parse(self, request):
        
        return (request.split(' ', 1)[0],
                request.split(' ', 2)[1],
                request.split('\r\n\r\n')[-1])

    def process(self, parsed):
       
        method, resourceName, body = parsed


        if (method == "GET"):
            try:
                if (self.operacion == "+"):
                    Resultado = int(self.op1) + int(self.op2)
                elif (self.operacion == "-"):
                    Resultado = int(self.op1) - int(self.op2)
                elif (self.operacion == "*"):
                    Resultado = int(self.op1) * int(self.op2)
                elif (self.operacion == "/"):
                    Resultado = int(self.op1) / int(self.op2)
                else:
                    Resultado = "Introduce la operacion que quieres hacer."

                httpCode = "200 OK"
                htmlBody = ("<html><body>" + str(self.op1) +
                            str(self.operacion) + str(self.op2) + " = " +
                            str(Resultado) + "</html>")
            except(ZeroDivisionError):
                httpCode = "200 OK"
                htmlBody = ("<html><body>Division entre cero</html>")

        elif (method == "PUT"):
            self.op1, self.op2, self.operacion = body.split(',')
            print("op1 = " + self.op1)
            print("op2 = " + self.op2)

            print("operac = " + self.operacion)
            httpCode = "200 OK"
            htmlBody = ("<html><body>La operación que quieres hacer: " +
                        str(self.op1) + str(self.operacion) +
                        str(self.op2) + "</html>")
        else:
            print("No se puede hacer otra operacion")
            httpCode = "405 Method Not Allowed"
            htmlBody = ("<html><body>operación  no valida " +
                        "</html>")

        return (httpCode, htmlBody)

if __name__ == "__main__":
    testWebApp = calc("localhost", 1234)