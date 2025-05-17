Knight Frank Wealth Report 2025 Dashboard
An interactive dashboard application that visualizes key insights and data from the Knight Frank Wealth Report 2025.

![Dashboard Preview](/public/placeholder.svg?height=400&width=800&query=Knight Frank Wealth Report Dashboard with charts and data visualizations)

Overview
This dashboard provides an interactive way to explore the Knight Frank Wealth Report 2025 data, including global wealth distribution, HNWI & UHNWI analysis, investment strategies, and prime residential market insights. The application is built with Next.js 15 and features responsive design, interactive charts, and comprehensive data visualization.

Features
Interactive Data Visualization: Explore wealth data through interactive charts and graphs
Comprehensive Analysis: Five key sections covering all aspects of the Wealth Report
PDF Export: Generate and download PDF reports of the dashboard data
PDF Import: Import and parse PDF reports to update dashboard data
Responsive Design: Optimized for desktop, tablet, and mobile devices
Dark Mode Support: Toggle between light and dark themes
Data Validation: Verify data sources and references
Tech Stack
Framework: Next.js 15 (App Router)
Styling: Tailwind CSS
UI Components: shadcn/ui
Charts: Chart.js
PDF Generation: jsPDF, html2canvas
State Management: React Hooks
Theming: next-themes
Getting Started
Prerequisites
Node.js 18.x or later
npm or pnpm
Installation
Clone the repository:
git clone https://github.com/your-username/knight-frank-dashboard.git
cd knight-frank-dashboard

I'll create a comprehensive README file for the Knight Frank Wealth Report 2025 Dashboard project:

```markdown project="Knight Frank Wealth Report Dashboard" file="README.md"
...
```

2. Install dependencies:


```shellscript
npm install
# or
pnpm install
```

3. Run the development server:


```shellscript
npm run dev
# or
pnpm dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser to see the dashboard.


## Project Structure

```plaintext
knight-frank-dashboard/
├── app/                    # Next.js App Router
│   ├── globals.css         # Global styles
│   ├── layout.tsx          # Root layout
│   └── page.tsx            # Home page
├── components/             # React components
│   ├── dashboard-layout.tsx # Main dashboard layout
│   ├── sections/           # Dashboard section components
│   ├── ui/                 # UI components (shadcn/ui)
│   └── visualizations/     # Chart and visualization components
├── hooks/                  # Custom React hooks
├── lib/                    # Utility functions
├── public/                 # Static assets
├── styles/                 # Additional styles
└── utils/                  # Utility functions for PDF generation, etc.
```

## Dashboard Sections

1. **Key Findings & Executive Summary**: Critical insights from the Wealth Report
2. **Global Wealth Landscape**: Analysis of global wealth trends and distribution
3. **HNWI & UHNWI Analysis**: Detailed breakdown of high-net-worth individuals
4. **Investment Strategies**: Analysis of investment preferences and asset allocation
5. **Prime Residential & Luxury Investments**: Analysis of prime property markets


## Features in Detail

### PDF Export

The dashboard includes functionality to generate and download a PDF report of the current dashboard state. Click the "Download Report" button in the sidebar to generate a PDF.

### PDF Import

You can import Knight Frank Wealth Report PDFs to extract and visualize the data. Click the "Import PDF Report" button in the sidebar to upload a PDF.

### Data Validation

The Data Validation sheet provides references to the source pages for each metric in the Knight Frank Wealth Report 2025, ensuring data accuracy and transparency.

### Theme Toggle

Toggle between light and dark themes using the theme toggle button in the top-right corner of the dashboard.

## Development

### Adding New Visualizations

To add a new visualization:

1. Create a new component in the `components/visualizations` directory
2. Import and use the Chart component from `@/components/ui/chart`
3. Add the visualization to the appropriate section component


### Modifying Data

Data is currently hardcoded in the components. To update with real data:

1. Modify the data constants in the relevant section components
2. Ensure the data structure matches the expected format for the charts


## Deployment

This project can be deployed on Vercel:

```shellscript
npm run build
# or
pnpm build
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Data sourced from the Knight Frank Wealth Report 2025
- UI components from [shadcn/ui](https://ui.shadcn.com/)
- Charts powered by [Chart.js](https://www.chartjs.org/)
- PDF generation using [jsPDF](https://github.com/parallax/jsPDF)


## Contact

For more information, visit [knightfrank.com/wealthreport](https://www.knightfrank.com/wealthreport)

```plaintext

This README provides a comprehensive overview of the Knight Frank Wealth Report 2025 Dashboard project, including its features, tech stack, installation instructions, and project structure. It will help users understand the purpose of the project and how to get started with it.



```
