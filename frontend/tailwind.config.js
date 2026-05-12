module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#f0f9ff",
          500: "#0ea5e9",
          600: "#0284c7",
          700: "#0369a1",
        },
        secondary: {
          50: "#f5f3ff",
          500: "#a78bfa",
          600: "#9333ea",
        },
      },
      fontFamily: {
        sans: ["Segoe UI", "Roboto", "sans-serif"],
      },
    },
  },
  plugins: [],
};
