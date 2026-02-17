import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                module1: resolve(__dirname, 'module1.html'),
                module2: resolve(__dirname, 'module2.html'),
            }
        }
    }
})
