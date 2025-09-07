import csv
import io
import os
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Gerador_csv

def gerar_csv_view(request):
    template_name = 'csvsequencial/page/csvsequencial.html'

    if request.method == 'POST':
        form = Gerador_csv(request.POST)

        if form.is_valid():
            dados_limpos = form.cleaned_data
            codigo_base = dados_limpos['codigo_base']
            caminho_base = dados_limpos['caminho']
            inicial = dados_limpos['quantidadeInicial']
            final = dados_limpos['quantidadeFinal']
            
            buffer_texto = io.StringIO()
            escritor_csv = csv.writer(buffer_texto)

            escritor_csv.writerow(['codigo', '@caminho'])

            numero_sequencial = inicial
            while numero_sequencial <= final:
                codigo_completo = f"{codigo_base}-{numero_sequencial:06d}"
                

                caminho_completo_bruto = os.path.join(caminho_base, f"{codigo_completo}.png")

                caminho_corrigido = caminho_completo_bruto.replace("\\", "/")

                escritor_csv.writerow([codigo_completo, caminho_corrigido])

                numero_sequencial = numero_sequencial + 1

            conteudo_csv = buffer_texto.getvalue()
            response = HttpResponse(conteudo_csv, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{codigo_base}.csv"'
            
            return response

    else:
        form = Gerador_csv()

    contexto = {
        'form': form,
    }

    return render(request, template_name, contexto)