# 🚀 Blog Flavio Macedo

Um blog moderno construído com **Django + Tailwind CSS v4**, focado em **Linux, tecnologia, economia e liberdade**.

---

## ✨ Preview

Interface moderna com:

* 🌙 Dark Mode automático
* ⚡ Design responsivo
* 🎨 UI elegante com Tailwind v4
* 🧠 Conteúdo voltado para pensamento crítico e tecnologia

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python + Django
* 🎨 Tailwind CSS v4
* ⚡ Alpine.js
* ✍️ Markdown + Pygments
* 📝 CKEditor 5 (admin)
* 🎯 Lucide Icons

---

## 📸 Features

* ✅ Hero section moderna e responsiva
* ✅ Sistema de tópicos dinâmicos
* ✅ Posts em destaque
* ✅ Dark Mode persistente (localStorage)
* ✅ Syntax Highlight para código
* ✅ Integração com Django Templates

---

## 🌙 Dark Mode

O tema escuro é ativado automaticamente com base em:

* Preferência do sistema
* Ou escolha manual do usuário

```javascript
if (
  localStorage.getItem('dark') === 'true' ||
  (!localStorage.getItem('dark') &&
    window.matchMedia('(prefers-color-scheme: dark)').matches)
) {
  document.documentElement.classList.add('dark')
}
```

---

## ⚙️ Setup do projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Flaviohmm/Blog_fm.git
cd blog_fm
```

---

### 2. Ambiente Python

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Setup do Tailwind v4

```bash
npm install
```

Rodar o build:

```bash
npx @tailwindcss/cli -i ./theme/static_src/src/input.css -o ./theme/static/css/output.css --watch
```

---

### 4. Rodar servidor

```bash
python manage.py migrate
python manage.py runserver
```

---

## 📁 Estrutura do projeto

```bash
theme/
 ├── static_src/
 │   └── src/
 │       └── input.css
 ├── static/
 │   └── css/
 │       └── output.css
templates/
 └── base.html
```

---

## 🧠 Highlight de código

O projeto usa:

* Markdown para conteúdo
* Pygments para cores

Geração do CSS:

```bash
pygmentize -S dracula -f html > static/css/pygments.css
```

---

## 🎨 UI/UX

* Gradientes modernos
* Micro-interações com hover
* Layout responsivo
* Tipografia com `prose` (Tailwind)

---

## 🚀 Roadmap

* [ ] Sistema de comentários
* [ ] Busca full-text
* [ ] Tags e categorias avançadas
* [ ] Editor Markdown com preview
* [ ] Deploy automático (CI/CD)

---

## 📄 Licença

Este projeto é open-source sob a licença MIT.

---

## 💡 Autor

**Flavio Macedo**

* Linux 🐧
* Tecnologia 💻
* Economia 📊
* Liberdade 🧠

---

## ⭐ Contribuição

Pull requests são bem-vindos!

Se você gostou do projeto, deixe uma ⭐ no repositório.
