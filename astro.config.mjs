import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://thecynic.io',
  integrations: [tailwind()],
  output: 'static',
});
