/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/js/**/*.js", 
  ],
  theme: {
    extend: {
      colors: {
        medicalGreen: "#6FCF97",
        medicalGreenDark: "#5ab07d",
      },
    },
  },
  plugins: [],
}

