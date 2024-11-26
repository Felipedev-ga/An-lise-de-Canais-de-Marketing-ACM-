import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimentos, cliques, conversoes):
        self.canal = canal
        self.investimentos = investimentos
        self.cliques = cliques
        self.conversoes = conversoes

    def cpc(self):
        return self.investimentos / self.cliques

campanhas = [
    Campanha('Facebook Ads', 1000, 15000, 150),
    Campanha('Google Ads', 1200, 10000, 200),
    Campanha('Email Ads', 5000, 5000, 50),
    Campanha('Instagram Ads', 800, 12000, 80),
]

canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]


plt.figure(figsize=(10, 6))
plt.bar(canais, cpcs, color=['blue', 'green', 'red', 'purple'])
plt.title('Custos por Clique', fontsize=16, fontweight='bold')
plt.xlabel('Canais', fontsize=12)
plt.ylabel('Custos em R$', fontsize=12)
plt.xticks(rotation=45)
media_cpc = sum(cpcs) / len(cpcs)
plt.axhline(media_cpc, color='orange', linestyle='--', label=f'Média CPC: R${media_cpc:.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('custos_por_clique.png', dpi=300)
plt.show()