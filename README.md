# knight-frank-dashboard### Knight Frank Wealth Report 2025 Dashboard

An interactive dashboard application built with Next.js that visualizes key insights from the Knight Frank Wealth Report 2025.





## Overview

This dashboard provides an interactive way to explore data from the Knight Frank Wealth Report 2025. It visualizes global wealth trends, HNWI/UHNWI analysis, investment strategies, and prime residential market performance through interactive charts and data tables.

## Features

- **Interactive Data Visualization**: Charts and graphs powered by Chart.js
- **Responsive Design**: Fully responsive layout that works on desktop and mobile devices
- **Section Navigation**: Easy navigation between different report sections
- **PDF Export**: Generate and download PDF reports of the dashboard data
- **PDF Import**: Import data from PDF reports to update the dashboard
- **Dark/Light Mode**: Toggle between dark and light themes


## Project Structure

```plaintext
knight-frank-dashboard/
├── app/                    # Next.js App Router files
├── components/             # React components
│   ├── sections/           # Dashboard section components
│   ├── ui/                 # UI components (shadcn/ui)
│   └── visualizations/     # Chart and data visualization components
├── hooks/                  # Custom React hooks
├── lib/                    # Utility functions
├── public/                 # Static assets
│   └── images/             # Images and icons
├── styles/                 # Global styles
└── utils/                  # Utility functions for PDF generation, etc.
```

## Main Sections

1. **Key Findings & Executive Summary**: Overview of critical insights from the report
2. **Global Wealth Landscape**: Analysis of global wealth trends and distribution
3. **HNWI & UHNWI Analysis**: Detailed breakdown of high-net-worth individuals
4. **Investment Strategies**: Analysis of investment preferences and asset allocation
5. **Prime Residential & Luxury Investments**: Analysis of prime property markets


## Technologies Used

- **Next.js 15**: React framework for building the application
- **TypeScript**: For type-safe code
- **Tailwind CSS**: For styling
- **shadcn/ui**: Component library
- **Chart.js**: For data visualization
- **jsPDF & html2canvas**: For PDF generation
- **Lucide React**: For icons


## Getting Started

### Prerequisites

- Node.js 18.0 or later
- npm or pnpm


### Installation

1. Clone the repository:

```shellscript
git clone https://github.com/your-username/knight-frank-dashboard.git
cd knight-frank-dashboard
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


## Building for Production

```shellscript
npm run build
# or
pnpm build
```

## Deployment

The project is configured for easy deployment on Vercel:

```shellscript
npm run build
npm run export
```

This will generate a static export in the `out` directory that can be deployed to any static hosting service.

## Data Sources

- Knight Frank Wealth Report 2025
- Knight Frank Prime International Residential Index (PIRI)
- Knight Frank Luxury Investment Index (KFLII)
- World Ultra Wealth Report 2024 (Wealth-X)
- Global Wealth Report 2024 (Credit Suisse)
- IMF World Economic Outlook


## License

This project is for demonstration purposes only. All data is sourced from the Knight Frank Wealth Report 2025 and associated research.

## Acknowledgements

- Dashboard created by Matthew Blackman with assistance from v0
- All data sourced from Knight Frank research
