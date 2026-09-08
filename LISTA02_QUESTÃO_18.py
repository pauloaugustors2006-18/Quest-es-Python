laboratorio_de_informatica = {
    "Equipamento 1": {
        "Equipamento": "Computador",
        "Marca": "Asus",
        "Situação": "Funcionando"
    },
    "Equipamento 2": {
        "Equipamento": "Impressora 3d",
        "Marca": "Bambu Lab",
        "Situação": "Em manutenção"
    }
}
for patrimonio, dados in laboratorio_de_informatica.items():
    print("Patrimônio:", patrimonio)
    print("Equipamento:", dados["Equipamento"])
    print("Marca:", dados["Marca"])
    print("Situação:", dados["Situação"])
    print(".\n")