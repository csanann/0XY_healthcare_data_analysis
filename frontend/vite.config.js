// /0XY_healthcare_data_analysis/frontend/vite.config.js
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 8081,
    cors: false,
    watch: {
      usePolling: true,
    },
  },
});