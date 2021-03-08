import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','simulador.settings')

import django
django.setup()

from app.models import District, Region, TicketBus

region_data = [
    "Continente", #1
    "Centro", #2
    "Norte", #3
    "Sul", #4
    "Leste" #5
]

region_district = [
    {
        "region":2,
        "district": [
            {"id":1, "name":"Centro"},
            {"id":13, "name":"José Mendes"},
            {"id":15, "name":"Agrônomica"},
            {"id":16, "name":"Trindade"},
            {"id":17, "name":"Santa Mônica"},
            {"id":18, "name":"Pantanal"},
            {"id":19, "name":"Córrego Grande"},
            {"id":21, "name":"Itacorubi"},
            {"id":22, "name":"Monte Verde"},
            {"id":23, "name":"João Paulo"},
            {"id":27, "name":"Saco Grande"}
        ]
    },{
    "region":1,
    "district": [
        {"id":2, "name":"Estreito"},
        {"id":3, "name":"Coqueiros"},
        {"id":4, "name":"Capoeiras"},
        {"id":5, "name":"Balneário"},
        {"id":6, "name":"Canto"},
        {"id":7, "name":"Jardim Atlântico"},
        {"id":8, "name":"Coloninha"},
        {"id":9, "name":"Monte Cristo"},
        {"id":10, "name":"Abraão"},
        {"id":11, "name":"Bom Abrigo"},
        {"id":12, "name":"Itaguaçu"}
    ]
    },{
    "region":3,
    "district": [
        {"id":28, "name":"Cacupé"},
        {"id":29, "name":"Santo Antônio"},
        {"id":30, "name":"Sambaqui"},
        {"id":31, "name":"Ratones"},
        {"id":32, "name":"Jurerê Internacional"},
        {"id":33, "name":"Daniela"},
        {"id":34, "name":"Praia do Forte"},
        {"id":35, "name":"Jurerê"},
        {"id":36, "name":"Canasvieiras"},
        {"id":37, "name":"Vargem Pequena"},
        {"id":38, "name":"Vargem Grande"},
        {"id":39, "name":"Vargem do Bom Jesus"},
        {"id":40, "name":"Cachoeira do Bom Jesus"},
        {"id":41, "name":"Ponta das Canas"},
        {"id":42, "name":"Praia Brava"},
        {"id":43, "name":"Ingleses do Rio Vermelho"},
        {"id":44, "name":"São João do Rio Vermelho"}
    ]
    },{
    "region":4,
    "district": [
        {"id":14, "name":"Saco dos Limões"},
        {"id":20, "name":"Costeira do Pirijubaé"},
        {"id":45, "name":"Rio Tavares"},
        {"id":46, "name":"Campeche"},
        {"id":47, "name":"Carianos"},
        {"id":48, "name":"Tapera"},
        {"id":49, "name":"Ribeirão da Ilha"},
        {"id":50, "name":"Morro das Pedras"},
        {"id":51, "name":"Armação e Pântano Sul"},
        {"id":52, "name":"Pântano Sul"}
    ]
    },{
    "region":5,
    "district": [
        {"id":24, "name":"Lagoa da Conceição"},
        {"id":25, "name":"Costa da Lagoa"},
        {"id":26, "name":"Barra da Lagoa"}
    ]
    }            
]

for region in region_data:
    data = Region(name=region)
    data.save()

for region in region_district:
    region_value = region.get('region')
    region_object = Region.objects.get(pk=region_value)
    for distri in region.get('district'):
        data = District(name=distri.get('name'), region=region_object)
        data.save()