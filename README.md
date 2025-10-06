# Robolog Automation Website

A modern, responsive React.js website for Robolog Automation - a leading provider of industrial software development, IoT solutions, and testing equipment.

## 🚀 Features

- **Modern Design**: Clean, professional design with smooth animations and transitions
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Interactive Components**: Engaging user interface with hover effects and animations
- **SEO Optimized**: Built with SEO best practices and semantic HTML
- **Fast Performance**: Optimized for speed and performance
- **Accessibility**: WCAG compliant with proper ARIA labels and keyboard navigation

## 🛠️ Technology Stack

- **Frontend**: React.js 18.2.0
- **Routing**: React Router DOM 6.3.0
- **Icons**: React Icons 4.4.0
- **Animations**: Framer Motion 7.2.1
- **Styling**: CSS3 with modern features
- **Build Tool**: Create React App

## 📁 Project Structure

```
src/
├── components/
│   ├── Header.js
│   ├── Header.css
│   ├── Footer.js
│   └── Footer.css
├── pages/
│   ├── Home.js
│   ├── Home.css
│   ├── About.js
│   ├── About.css
│   ├── Services.js
│   ├── Services.css
│   ├── Products.js
│   ├── Products.css
│   ├── Contact.js
│   └── Contact.css
├── App.js
├── App.css
├── index.js
└── index.css
```

## 🚀 Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd robolog-automation-website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000` to view the website.

### Build for Production

```bash
npm run build
```

This creates a `build` folder with optimized production files.

## 📱 Pages Overview

### 🏠 Home Page
- Hero section with compelling call-to-action
- Features showcase with animated cards
- Services overview with detailed descriptions
- Products highlight with pricing
- Statistics and achievements
- Call-to-action sections

### ℹ️ About Page
- Company story and mission
- Core values and principles
- Team information
- Achievements and milestones
- Company culture highlights

### 🛠️ Services Page
- Detailed service descriptions
- Specialized solutions
- Technology stack
- Process methodology
- Service comparison

### 📦 Products Page
- Featured products with pricing
- IoT sensors and devices
- Testing equipment
- Software solutions
- Product comparison table

### 📞 Contact Page
- Contact information and form
- Interactive contact form with validation
- Social media links
- FAQ section
- Map integration placeholder

## 🎨 Design Features

### Color Scheme
- **Primary**: #007bff (Blue)
- **Secondary**: #28a745 (Green)
- **Accent**: #dc3545 (Red)
- **Gradient**: Various gradient combinations for visual appeal

### Typography
- **Font Family**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800
- **Responsive**: Scales appropriately across devices

### Animations
- Scroll-triggered animations
- Hover effects on interactive elements
- Smooth transitions between states
- Loading animations and micro-interactions

## 📱 Responsive Design

The website is fully responsive and optimized for:
- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

## 🔧 Customization

### Adding New Pages
1. Create a new component in the `src/pages/` directory
2. Add the route in `src/App.js`
3. Create corresponding CSS file
4. Update navigation in `src/components/Header.js`

### Modifying Styles
- Global styles: `src/index.css`
- Component styles: Individual CSS files
- App-wide styles: `src/App.css`

### Adding New Features
- Create new components in `src/components/`
- Follow the existing naming conventions
- Use the established design patterns

## 🚀 Deployment

### Netlify
1. Build the project: `npm run build`
2. Upload the `build` folder to Netlify
3. Configure redirects for client-side routing

### Vercel
1. Connect your GitHub repository
2. Vercel will automatically detect React and build
3. Deploy with zero configuration

### GitHub Pages
1. Install gh-pages: `npm install --save-dev gh-pages`
2. Add deploy script to package.json
3. Run: `npm run deploy`

## 📊 Performance Optimization

- **Code Splitting**: Automatic code splitting with React Router
- **Image Optimization**: Optimized images and lazy loading
- **CSS Optimization**: Minified and optimized CSS
- **Bundle Analysis**: Use `npm run build` to analyze bundle size

## 🔍 SEO Features

- Semantic HTML structure
- Meta tags and descriptions
- Open Graph tags
- Structured data markup
- Sitemap generation ready

## 🛡️ Security

- No sensitive data in client-side code
- Secure form handling
- XSS protection
- CSRF protection ready

## 📈 Analytics Ready

The website is ready for analytics integration:
- Google Analytics
- Facebook Pixel
- Custom tracking solutions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Email: info@robolog.co.in
- Phone: +1 (555) 123-4567
- Website: https://www.robolog.co.in

## 🙏 Acknowledgments

- React.js community for excellent documentation
- React Icons for comprehensive icon library
- Google Fonts for typography
- All contributors and supporters

---

**Built with ❤️ by Robolog Automation Team**

## Backend (Django) for Contact Form

The repository includes a minimal Django backend to receive contact submissions.

### Setup

1) Create and activate venv (Windows PowerShell):

```
python -m venv venv
venv\Scripts\Activate.ps1
```

2) Install dependencies:

```
venv\Scripts\pip install django djangorestframework django-cors-headers
```

3) Run migrations and start the server:

```
venv\Scripts\python manage.py migrate
venv\Scripts\python manage.py runserver
```

API endpoint: `http://127.0.0.1:8000/api/contact/` (POST). The React `Contact` form submits here.
