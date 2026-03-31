from typing import Any

from django.core.management.base import BaseCommand
from django.utils.text import slugify
import markdown

from blog.models import Post, Category, Tag


class Command(BaseCommand):
    help = 'Importa os 6 posts do arquivo posts.ts para o banco de dados'

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write(self.style.SUCCESS('Iniciando importação dos posts...'))

        # ==================== DADOS DOS POSTS ====================
        posts_data = [
            {
                "slug": "por-que-migrei-para-linux-2026",
                "title": "Por que migrei 100% para Linux em 2026",
                "excerpt": "Após anos alternando entre Windows e Linux, finalmente dei o passo definitivo. Aqui conto como foi a transição e o que aprendi.",
                "category": "Linux",
                "read_time": 5,
                "tags": ["Linux", "Open Source", "Produtividade"],
                "content": """## Introdução
                    Depois de mais de uma década usando Windows como sistema principal, 2026 foi o ano em que finalmente migrei 100% para Linux. Não foi uma decisão impulsiva — foi o resultado de anos testando distribuições, aprendendo sobre o ecossistema e, acima de tudo, valorizando cada vez mais a **liberdade de controle** sobre minha própria máquina.

                    ## O que motivou a mudança
                    A motivação veio de vários fatores que se acumularam ao longo do tempo:
                    - **Privacidade**: O Windows se tornou cada vez mais invasivo em termos de telemetria e coleta de dados.
                    - **Performance**: Meu hardware rodava significativamente melhor no Linux.
                    - **Filosofia**: Como defensor da liberdade individual, usar software proprietário que me trata como produto começou a soar contraditório.

                    ## A escolha da distribuição
                    Testei diversas distros ao longo dos anos:
                    ### Arch Linux
                    O Arch foi minha escola. Aprendi mais sobre como um sistema operacional funciona instalando Arch do que em qualquer curso.

                    ### Fedora
                    Fedora oferece um excelente equilíbrio entre estabilidade e software atualizado.

                    ### NixOS
                    Minha escolha final. O NixOS traz um paradigma completamente diferente: **configuração declarativa e reproduzível**.

                    ## Conclusão
                    A migração para Linux não é apenas uma escolha técnica — é uma declaração de valores.
                    > "A liberdade não é dada, é conquistada — inclusive no mundo digital."""
            },
            {
                "slug": "bitcoin-reserva-de-valor",
                "title": "Bitcoin como reserva de valor: uma análise racional",
                "excerpt": "Sem hype, sem maximismo. Uma análise fria e racional sobre o papel do Bitcoin como ativo de proteção patrimonial.",
                "category": "Economia",
                "read_time": 8,
                "tags": ["Bitcoin", "Investimentos", "Economia"],
                "content": """## Introdução
                    O debate sobre Bitcoin frequentemente oscila entre dois extremos. A verdade está no meio.

                    ## O que torna o Bitcoin único
                    ### Escassez programática
                    Oferta limitada a 21 milhões de unidades.

                    ### Descentralização
                    Nenhum governo ou empresa controla a rede.

                    ## Bitcoin vs. Ouro
                    Bitcoin supera o ouro em divisibilidade, portabilidade e verificabilidade.

                    ## Estratégia racional
                    Para um investidor racional, Bitcoin pode fazer sentido como 1% a 10% do portfólio, usando DCA e cold wallet.

                    ## Conclusão
                    Bitcoin é uma tecnologia monetária com propriedades únicas que o tornam uma opção racional de diversificação."""
            },
            {
                "slug": "self-hosting-liberdade-digital",
                "title": "Self-hosting: liberdade digital na prática",
                "excerpt": "Como montar seu próprio servidor para email, cloud storage e mais, usando Docker e Linux.",
                "category": "Tecnologia",
                "read_time": 6,
                "tags": ["Self-hosting", "Docker", "Linux"],
                "content": """## Introdução
                    Self-hosting é o ato de hospedar seus próprios serviços digitais.

                    ## Por que self-hosting?
                    - Privacidade
                    - Liberdade
                    - Aprendizado

                    ## Stack recomendada
                    - Hardware: Mini PC com Intel N100
                    - OS: Debian 12
                    - Docker + Traefik
                    - Serviços: Nextcloud, Vaultwarden, Immich, Uptime Kuma

                    ## Segurança essencial
                    1. Firewall
                    2. Atualizações automáticas
                    3. Backups 3-2-1
                    4. SSH com chave
                    5. VPN (WireGuard)

                    ## Conclusão
                    Self-hosting é um investimento em soberania digital."""
            },
            {
                "slug": "liberalismo-classico-seculo-xxi",
                "title": "O liberalismo clássico no século XXI",
                "excerpt": "Por que os princípios de liberdade individual e economia de mercado continuam mais relevantes do que nunca.",
                "category": "Política",
                "read_time": 7,
                "tags": ["Liberalismo", "Política", "Liberdade"],
                "content": """## Introdução
                    O liberalismo clássico é frequentemente mal compreendido.

                    ## Pilares
                    - Liberdade individual
                    - Propriedade privada
                    - Governo limitado
                    - Livre mercado

                    ## Aplicações no Brasil
                    - Carga tributária absurda
                    - Burocracia paralisante
                    - Protecionismo

                    ## Conclusão
                    O liberalismo clássico é um framework pragmático para maximizar liberdade e prosperidade."""
            },
            {
                "slug": "rust-vs-go",
                "title": "Rust vs Go: quando usar cada um?",
                "excerpt": "Uma comparação prática entre duas das linguagens mais promissoras para sistemas e backend.",
                "category": "Tecnologia",
                "read_time": 10,
                "tags": ["Rust", "Go", "Backend"],
                "content": """## Introdução
                    Rust e Go são complementares, não competidoras.

                    ## Go: simplicidade e produtividade
                    Ideal para APIs, microserviços e ferramentas CLI.

                    ## Rust: performance e segurança
                    Ideal para sistemas de alta performance e segurança crítica.

                    ## Comparação
                    | Aspecto | Go | Rust |
                    |---------|----|------|
                    | Curva de aprendizado | Fácil | Difícil |
                    | Performance | Muito boa | Excelente |

                    ## Conclusão
                    Use Go para velocidade de desenvolvimento. Use Rust quando performance e segurança são críticas."""
            },
            {
                "slug": "privacidade-digital-guia-2026",
                "title": "Privacidade digital: guia essencial 2026",
                "excerpt": "Ferramentas, práticas e mindset para proteger seus dados no mundo digital moderno.",
                "category": "Privacidade",
                "read_time": 9,
                "tags": ["Privacidade", "Segurança", "Ferramentas"],
                "content": """## Introdução
                    Em 2026, proteger sua privacidade é higiene digital básica.

                    ## Fundamentos
                    - Defina seu modelo de ameaças
                    - Privacidade é um espectro

                    ## Ferramentas essenciais
                    - Navegador: Firefox hardened ou Librewolf
                    - Mensagens: Signal
                    - Email: ProtonMail
                    - VPN: Mullvad
                    - DNS: NextDNS ou Pi-hole

                    ## Práticas diárias
                    - Use DuckDuckGo
                    - Minimize redes sociais
                    - Revise permissões de apps
                    - Use email aliases

                    ## Conclusão
                    Cada passo conta. Comece pequeno e avance gradualmente."""
            },
        ]

        for data in posts_data:
            # Cria ou obtém a categoria
            category_obj, _ = Category.objects.get_or_create(
                name=data["category"],
                defaults={"slug": slugify(data["category"])}
            )

            # Converte Markdown para HTML
            html_content = markdown.markdown(
                data["category"],
                extensions=['extra', 'codehilite', 'toc', 'tables']
            )

            # Cria ou atualiza o post
            post, created = Post.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "title": data["title"],
                    "excerpt": data["excerpt"],
                    "content": html_content,
                    "read_time": data["read_time"],
                    "category": category_obj,
                }
            )

            # Adiciona tags
            for tag_name in data.get("tags", []):
                tag_obj, _ = Tag.objects.get_or_create(
                    name=tag_name,
                    defaults={"slug": slugify(tag_name)}
                )
                post.tags.add(tag_obj)

            status = "✅ Criado" if created else "🔄 Atualizado"
            self.stdout.write(self.style.SUCCESS(f"{status}: {post.title}"))

        self.stdout.write(self.style.SUCCESS("\nImportação concluída com sucesso!"))