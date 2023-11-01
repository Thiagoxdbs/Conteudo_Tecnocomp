import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

css = ''
conteudo = input("CONTEUDO:\n")
assunto = input("ASSUNTO:\n")
remetente = input("DESTINATARIO:\n")


email = outlook.CreateItem(0)
email.To = remetente
email.Subject = f"{assunto}"
email.HTMLBody = f'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            {css}
        </head>
        <body>
            <section class="email">

                {conteudo}

            </section>
        </body>
    </html>
'''

email.Send()
print("OK")