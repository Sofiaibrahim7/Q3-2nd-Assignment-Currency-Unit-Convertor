import streamlit as st
from PIL import Image

# Custom CSS for improved UI
st.markdown(
    """
    <style>
   
    
        .stApp {
            background: linear-gradient(135deg, #2E3192, #1BFFFF);
        }
    
    
    unsafe_allow_html=True
)

        /* Sidebar color */
        .css-1d391kg {
            background-color:rgb(26, 24, 24) !important;
        }

        /* Main text color */
        .stMarkdown, .stTextInput label, .stSelectbox label {
            color: #2B6777;
        }

        /* Button Hover Effect */
        
        .stButton>button:hover {
            background-color: #21525D;
        }
    
    body {
        font-family: 'Arial', sans-serif;
        background-color: #0d1117;
        color: white;
    }
    .stButton>button {
        background:rgb(20, 238, 194) !important;
        color: white !important;
        font-size: 35px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        padding: 5px 6px !important;
        width: 100% !important;
        text-align: center !important;
        display: block !important;
        margin: auto !important;
        box-shadow: 0px 6px 15px rgba(26, 188, 156, 0.4);
    }
    .stButton>button:hover {
        background: #16a085 !important;
        transform: scale(1.12);
        transition: all 0.3s ease-in-out;
    }
    .stSelectbox>div {
        border-radius: 10px;
        padding: 8px;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
    }
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        display: flex;
        align-items: center;
    }
    .sidebar-title img {
        width: 25px;
        height: 25px;
        margin-right: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for converter selection before categories
st.sidebar.markdown("<div class='sidebar-title'>Select Converter</div>", unsafe_allow_html=True)
option = st.sidebar.radio("", ["💱 Currency Converter", "📐 Unit Converter"], index=1)

if option == "💱 Currency Converter":
    st.header("💱 Currency Converter")
    st.write("Developed by Sofia Ibrahim")
    currency_list = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY","PKR" "CNY", "CHF", "NZD", "ZAR", "SGD", "HKD", "NOK", "SEK", "DKK", "RUB", "BRL", "MXN", "MYR", "THB", "IDR", "PHP", "PLN", "TRY", "HUF", "CZK", "ILS", "CLP", "PEN", "COP", "SAR", "AED", "ARS", "EGP", "NGN", "PKR", "BDT", "VND"]
    c1, c2 = st.columns(2)
    with c1:
        amount = st.number_input("Enter amount", min_value=1.0)
    with c2:
        currency_from = st.selectbox("From", currency_list)
    currency_to = st.selectbox("To", currency_list)
    if st.button("Convert"):
        converted_amount = amount * 1.2  # Placeholder conversion rate
        st.success(f"✅ Converted Value: {converted_amount} {currency_to}")
else:
    # Sidebar for categories
    st.sidebar.markdown('<div class="sidebar-title"><img src="https://cdn-icons-png.flaticon.com/512/189/189715.png"> 🏷️ Categories</div>', unsafe_allow_html=True)
    categories = ["📏 Length", "💧 Liquid", "⚖️ Density", "⚡ Voltage", "🌡️ Temperature", "🎛️ Pressure", "🔋 Energy", "🚀 Speed", "🔩 Torque", "📐 Area", "📦 Volume", "⏱️ Time", "🎚️ Frequency", "📡 Data", "🎯 Angle", "🔄 Rotation", "📊 Power", "💡 Luminance", "🔊 Sound", "📞 Signal", "⚖️ Mass", "🔌 Electrical Resistance", "🔋 Electrical Capacitance", "⚙️ Mechanical Stress", "🧪 Chemistry", "🌍 Geology", "🩺 Medical", "🛠 Engineering", "🎮 Gaming Units", "🚗 Automotive"]

    category = st.sidebar.radio("Select Category", categories)

    # Dynamic conversion options
    conversion_units = {
        "📏 Length": ["Meter", "Centimeter", "Kilometer", "Mile", "Foot", "Inch"],
        "💧 Liquid": ["Liter", "Milliliter", "Gallon", "Pint"],
        "⚖️ Density": ["Kg/m³", "g/cm³", "lb/ft³"],
        "⚡ Voltage": ["Volt", "Millivolt", "Kilovolt"],
        "🌡️ Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "🎛️ Pressure": ["Pascal", "Bar", "PSI"],
        "🔋 Energy": ["Joule", "Kilojoule", "Calorie", "Kilocalorie"],
        "🚀 Speed": ["Meter/second", "Kilometer/hour", "Mile/hour", "Knot"],
        "🔩 Torque": ["Newton meter", "Foot-pound", "Inch-pound"],
        "📐 Area": ["Square meter", "Square kilometer", "Square mile", "Acre", "Hectare"],
        "📦 Volume": ["Cubic meter", "Cubic centimeter", "Cubic inch", "Cubic foot"],
        "⏱️ Time": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        "🎚️ Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
        "📡 Data": ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
        "🎯 Angle": ["Degree", "Radian", "Gradian"],
        "🔄 Rotation": ["Revolution", "Degree", "Radian"],
        "📊 Power": ["Watt", "Kilowatt", "Horsepower"],
        "💡 Luminance": ["Candela", "Lumen", "Lux"],
        "🔊 Sound": ["Decibel", "Sone", "Phon"],
        "📞 Signal": ["Decibel", "Bel"],
        "⚖️ Mass": ["Gram", "Kilogram", "Pound", "Ounce"],
        "🔌 Electrical Resistance": ["Ohm", "Milliohm", "Kiloohm"],
        "🔋 Electrical Capacitance": ["Farad", "Microfarad", "Nanofarad"],
        "⚙️ Mechanical Stress": ["Pascal", "Kilopascal", "Megapascal"],
        "🧪 Chemistry": ["Mole", "Millimole", "Micromole"],
        "🌍 Geology": ["Meter", "Kilometer", "Mile"],
        "🩺 Medical": ["Milligram", "Gram", "Kilogram"],
        "🛠 Engineering": ["Newton", "Kilonewton", "Meganewton"],
        "🎮 Gaming Units": ["Pixel", "Frame", "Polygon"],
        "🚗 Automotive": ["Horsepower", "Kilowatt", "Newton meter"]
    }

    # Main layout
    st.header("🚀 Modern Unit Converter")
    st.write("Developed by Sofia Ibrahim")
    st.header(f"{category} Converter")
    units_available = conversion_units.get(category, [])
    if not units_available:
        st.warning("🚨 No units available for this category! Please update the unit list.")
    else:
        c1, c2 = st.columns(2)
        with c1:
            value = st.number_input("Enter value", min_value=1.0)
        with c2:
            unit_from = st.selectbox("From", units_available)
        unit_to = st.selectbox("To", units_available)
        if st.button("Convert"):
            converted_value = value  # Placeholder for actual conversion logic
            st.success(f"✅ Converted Value: {converted_value} {unit_to}")
