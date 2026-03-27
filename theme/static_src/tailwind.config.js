/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',                    // ← Essencial para o toggle dark/light

  content: [
    // Todos os templates Django
    '../../templates/**/*.html',
    '../../blog/templates/**/*.html',
    '../../**/templates/**/*.html',

    // Se você usar JavaScript com classes Tailwind
    '../../static/js/**/*.js',
  ],

  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system_ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      colors: {
        // Opcional: você pode mapear as variáveis CSS aqui também
        border: 'hsl(var(--border))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        card: 'hsl(var(--card))',
        'card-foreground': 'hsl(var(--card-foreground))',
        muted: 'hsl(var(--muted))',
        'muted-foreground': 'hsl(var(--muted-foreground))',
        primary: 'hsl(var(--primary))',
        'primary-foreground': 'hsl(var(--primary-foreground))',
      },
    },
  },

  plugins: [],
}