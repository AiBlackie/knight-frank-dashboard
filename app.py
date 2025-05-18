import streamlit as st
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO

# --- Constants ---
V0_DEV_URL = "https://v0-app-data-recovery.vercel.app/"
LOGO_URL_SVG = "https://www.knightfrank.com/library/v3.0/images/knightfranklogo.svg"
VERSION = "2.0"
LAST_UPDATED = "2025-05-17"
WEALTH_REPORT_2025_VIDEO = "https://www.youtube.com/watch?v=yyftb8A4Dt8"

# --- Page Configuration ---
st.set_page_config(
    page_title="Terra Caribbean Wealth Insights",
    page_icon="🏝️",
    layout="wide"
)

# --- Helper Functions ---
@st.cache_data(ttl=86400)
def load_raster_image_from_url(image_url: str):
    """
    Loads a raster image (PNG, JPEG) from a URL using PIL.
    This function is cached. It will not work for SVGs.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(image_url, headers=headers, timeout=10)
       
        print(f"Attempting to load RASTER image from: {image_url}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content-Type: {response.headers.get('Content-Type')}")
       
        response.raise_for_status()

        if not response.content:
            st.warning("Image content is empty.")
            return None
       
        logo_image = Image.open(BytesIO(response.content))
        return logo_image
       
    except requests.exceptions.HTTPError as http_err:
        st.warning(f"HTTP error occurred while loading image: {str(http_err)}")
        print(f"HTTP error: {str(http_err)} - URL: {image_url}")
        return None
    except requests.exceptions.RequestException as req_err:
        st.warning(f"Network error occurred while loading image: {str(req_err)}")
        print(f"Request error: {str(req_err)} - URL: {image_url}")
        return None
    except UnidentifiedImageError:
        st.warning(f"Cannot identify image file from URL: {image_url}. It might be an unsupported format (like SVG) for PIL, or corrupted.")
        print(f"PIL UnidentifiedImageError. URL: {image_url}, Content-Type: {response.headers.get('Content-Type') if 'response' in locals() else 'N/A'}")
        return None
    except Exception as e:
        st.warning(f"An unexpected error occurred while loading image: {str(e)}")
        print(f"Generic error loading image: {type(e).__name__} - {str(e)} - URL: {image_url}")
        return None

# --- Main Application UI ---
st.title("Wealth Report 2025")
st.caption("Premium Luxury Real Estate Analytics by Terra Caribbean, leveraging Knight Frank insights.")

# --- Version & Disclaimer ---
st.warning(f"""
**Version {VERSION} | Disclaimer**  
This dashboard uses preliminary data from the Knight Frank Wealth Report 2025.  
While based on real sources, figures may contain errors or approximations.  
*This is a demo under active testing—verify critical metrics with official reports.*  
""")

col1, col2 = st.columns([1, 5])

with col1:
    st.image(LOGO_URL_SVG, width=150, use_container_width=False)  # Updated parameter here

with col2:
    st.markdown("""
    ### Global Wealth Trends
    Explore high-net-worth individual (HNWI) demographics and prime property performance.
    """)

# Add the 2025 video link button
st.link_button("📺 Watch the 2025 Wealth Report Highlights", WEALTH_REPORT_2025_VIDEO, 
              help="Official Knight Frank Wealth Report 2025 video overview")

st.divider()

# --- Embedded Dashboard ---
st.subheader("Global Wealth Dashboard")
st.markdown("""
**Interactive visualization of HNWI trends and prime residential markets.**  
*Powered by v0.dev • Data refreshed quarterly.*  
""")

st.link_button("🚀 Open Full Dashboard", V0_DEV_URL)

try:
    st.components.v1.iframe(
        V0_DEV_URL,
        width=None,
        height=600,
        scrolling=True
    )
except Exception as e:
    st.error(f"Could not load the interactive dashboard. Please try again later or check the URL. Error: {e}")

# --- Footer ---
st.divider()
st.markdown(f"""
---
**Credits & Contact**  
- **Data Source:** [Knight Frank Wealth Report 2025](https://www.knightfrank.com/wealthreport)  
- **Video Overview:** [2025 Wealth Report Highlights]({WEALTH_REPORT_2025_VIDEO})  
- **Version:** {VERSION} | Last updated: {LAST_UPDATED}  

*For verified data, refer to official Knight Frank publications.*  
""")