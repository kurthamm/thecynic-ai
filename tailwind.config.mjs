/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        lantern: {
          50: '#fdf8ef',
          100: '#fbf0d9',
          200: '#f6ddb3',
          300: '#f0c682',
          400: '#e9a84e',
          500: '#e3912b',
          600: '#d57721',
          700: '#b15c1d',
          800: '#8d4a1f',
          900: '#733e1c',
        },
        dark: {
          50: '#f6f6f9',
          100: '#ededf1',
          200: '#d7d7e0',
          300: '#b3b4c5',
          400: '#8a8ba5',
          500: '#6b6c8b',
          600: '#565673',
          700: '#46465e',
          800: '#3c3c4f',
          900: '#1a1a2e',
          950: '#0f0f1a',
        },
      },
      fontFamily: {
        serif: ['Playfair Display', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
};
