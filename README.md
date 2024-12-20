# FastHTML Tailwind CSS Integration

Welcome to the **FastHTML Tailwind CSS** integration project! This repository offers components and templates to seamlessly integrate **Tailwind CSS** into your FastHTML projects. Tailwind CSS is a utility-first CSS framework designed to provide unparalleled flexibility and speed in styling your applications.

---

## 📦 Installation

### Step 1: Install Tailwind CSS
Tailwind CSS requires **Node.js** as a dependency. Follow the steps below to install and configure Tailwind CSS for your project.

#### 1.1 Install Tailwind CSS via npm
Run the following commands in your terminal:
```bash
npm install -D tailwindcss
npx tailwindcss init
```

#### 1.2 Configure Template Paths
Update your `tailwind.config.js` file with the paths to your template files:
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

#### 1.3 Add Tailwind Directives to Your CSS
Include the Tailwind CSS directives in your main CSS file (`src/input.css`):
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

#### 1.4 Start the Tailwind CLI Build Process
Run the following command to start the Tailwind CSS build process:
```bash
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

#### 1.5 Use Custom CSS from fh_tailwindcss

To customize your styles, follow these steps:

Copy the tailwind.css.template file and paste it into your CSS folder.

Import the tailwind.css file into your input.css:
```css
@import './src/static/css/tailwind.css';
```
It will look like this:
```css
/* Add your Tailwind directives if needed */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* input.css */
@import './src/static/css/tailwind.css';
```

### Step 2: Integrate Tailwind CSS into FastHTML

#### 2.1 Link the Compiled CSS File
Include the compiled CSS file in the `<head>` of your FastHTML app:
```python
app, rt = fast_app(
    pico=False,  # We're using Tailwind CSS instead of PicoCSS
    hdrs=(
        Meta(charset="UTF-8"),
        Meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
        ),
        Meta(
            name="description",
            content="FastHTML template using Tailwind CSS for styling",
        ),
        Link(rel="stylesheet", href="/static/css/output.css", type="text/css"),
    ),
    static_path=Path(__file__).parent / "static",
)
```

#### 2.2 Use Tailwind Utility Classes
You can now use Tailwind CSS classes to style your FastHTML templates and components. Here is an example of a styled button:
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Click Me
</button>
```

---

## 🌟 Features
- **Utility-First Approach:** Tailwind CSS provides a rich set of utility classes for rapid UI development.
- **Customizable Design:** Extend Tailwind's default configuration to match your project's unique needs.
- **Seamless Integration:** Quickly add Tailwind CSS to your FastHTML templates and components.
- **Real-Time Updates:** Leverage the Tailwind CLI for real-time CSS updates during development.

---

## ✨ Custom Build Components
This repository provides a set of custom-built components to enhance your development experience. For example, the **Modal** component:

```python
from fasthtml.common import *
from fh_tailwindcss import GridContainer, LabeledInput

@rt("/")
def get():
    return Form(
        GridContainer(2,
            LabeledInput("User Name", id="user-id", type="text"),
            LabeledInput("Email", id="email", type="email")),
        GridContainer(1,
            LabeledTextarea("Description", id="description", rows=4)))
```

---

## 🚀 Getting Started
To get started, clone this repository and follow the installation steps above. Feel free to explore and contribute by adding new components or optimizing the existing templates.

```bash
git clone https://github.com/Epic-Codebase/fh_tailwind.git
```

---

## 🛠️ Contributing
Contributions are welcome! If you have ideas for new components or improvements, please open an issue or submit a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### 🙌 Acknowledgments
Special thanks to the creators of Tailwind CSS and FastHTML for their amazing tools that make development faster and more enjoyable.

