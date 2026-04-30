# 🚀 Senior QA Automation Framework - InheritX Website

## 📋 Framework Overview

A **production-grade, scalable automation framework** designed for comprehensive website validation including header extraction, dynamic navigation handling, and data persistence.

### Key Features
✅ **Reusable Page Objects** - HeaderPage, NavigationPage with extensible BasePage  
✅ **Dynamic Navigation** - Non-hardcoded menu item detection and navigation  
✅ **Data Extraction** - Email, phone, company info extraction with validation  
✅ **Visual Highlighting** - CSS-based element highlighting with screenshots  
✅ **Soft Assertions** - Continue testing even on assertion failures  
✅ **Structured Logging** - All-encompassing test execution logs  
✅ **JSON Reporting** - Structured data export for analysis  
✅ **Allure Reporting** - Beautiful test reports with screenshots

---

## 📁 Project Structure

```
playwright-framework/
│
├── pages/
│   ├── base_page.py           # Enhanced base class with 30+ methods
│   ├── header_page.py         # Header extraction and validation
│   ├── navigation_page.py     # Dynamic navigation handling
│   ├── login_page.py          # Legacy page object
│   └── locators/
│       └── login_locators.py  # Centralized locators
│
├── tests/
│   └── test_login.py          # Comprehensive test suite with 4 tests
│
├── utils/
│   ├── config.py              # Configuration management
│   ├── logger.py              # Structured logging
│   ├── assertions.py          # Soft assertions library
│   ├── data_extractor.py      # Data extraction & validation
│   ├── excel_utils.py         # Excel file handling
│   ├── json_utils.py          # JSON file handling
│   └── db_utils.py            # Database operations
│
├── testdata/
│   └── login_data.xlsx        # Test data repository
│
├── conftest.py                # Pytest fixtures and hooks
├── pytest.ini                 # Pytest configuration
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
# Navigate to project directory
cd playwright-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 2. Configure Environment

Edit `.env` file:
```
BASE_URL=https://www.inheritx.com
BROWSER=chromium
HEADLESS=false
TIMEOUT=30000
USERNAME=user
PASSWORD=password
```

### 3. Verify Installation

```bash
pytest --version
allure --version
```

---

## 🧪 Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test
```bash
# Header validation
pytest tests/test_login.py::TestInheritXFramework::test_header_validation_and_data_extraction -v

# Navigation structure
pytest tests/test_login.py::TestInheritXFramework::test_navigation_structure_and_dynamics -v

# Full navigation
pytest tests/test_login.py::TestInheritXFramework::test_navigate_all_sections -v

# Complete validation
pytest tests/test_login.py::TestInheritXFramework::test_complete_website_validation -v
```

### Run with Allure Reporting
```bash
# Run tests and generate Allure results
pytest tests/ -v --alluredir=allure-results

# View Allure report
allure serve allure-results
```

### Run Tests in Parallel
```bash
pytest tests/ -v -n auto
```

### Run with Specific Browser
```bash
# Firefox
BROWSER=firefox pytest tests/ -v

# WebKit
BROWSER=webkit pytest tests/ -v
```

---

## 🏗️ Framework Architecture

### BasePage (Enhanced Base Class)

Enhanced with **30+ methods** for senior-level automation:

#### Navigation Methods
- `open_url(url)` - Navigate with automatic wait
- `get_title()` - Get page title
- `get_current_url()` - Get current URL
- `refresh_page()` - Reload page
- `go_back()` / `go_forward()` - Browser navigation

#### Interaction Methods
- `click(locator)` - Click element with logging
- `enter_text(locator, text)` - Fill text input
- `hover(locator)` - Hover over element
- `hover_and_wait(locator, wait_for)` - Hover and wait for element

#### Retrieval Methods
- `get_text(locator)` - Get element text
- `get_all_texts(locator)` - Get all matching elements text
- `get_attribute(locator, attr)` - Get attribute value
- `get_count(locator)` - Count matching elements

#### Wait Methods
- `wait_for_element(locator, timeout)` - Wait for element attachment
- `wait_for_visible(locator, timeout)` - Wait for visibility
- `wait_for_load_state(state)` - Wait for page load state

#### Visual Methods
- `take_screenshot(name)` - Timestamped screenshot
- `take_element_screenshot(locator, name)` - Element-specific screenshot
- `highlight_element(locator)` - CSS-based red border highlight
- `highlight_and_screenshot(locator, name)` - Highlight + Screenshot

#### Scroll Methods
- `scroll_to_element(locator)` - Scroll element into view
- `scroll_to_top()` / `scroll_to_bottom()` - Page scroll

#### Validation Methods
- `element_exists(locator)` - Check element existence
- `verify_text_present(text)` - Verify text on page
- `verify_text_not_present(text)` - Verify text absence

---

### HeaderPage Component

**Purpose**: Extract and validate header information

```python
header_page = HeaderPage(page)

# Extract company info
company_info = header_page.extract_company_info()
# Returns: {"name": "InheritX", "logo_alt": "InheritX Logo"}

# Extract contact info
contact_info = header_page.extract_contact_information()
# Returns: {"emails": [...], "phones": [...]}

# Validate contact info
validation = header_page.validate_contact_information(contact_info)
# Returns: {"emails_valid": [...], "phones_valid": [...], ...}

# Get complete header data with all validations
complete_data = header_page.get_complete_header_data()
```

---

### NavigationPage Component

**Purpose**: Dynamic navigation structure and menu handling

```python
nav_page = NavigationPage(page)

# Capture all menu items (dynamic, not hardcoded)
menu_items = nav_page.capture_all_menu_items()
# Returns: ["About Us", "Services", "Portfolio", ...]

# Identify dropdown menus
dropdowns = nav_page.identify_dropdowns()
# Returns: [{"name": "Services", "has_submenu": True}, ...]

# Navigate to specific section
result = nav_page.navigate_to_section("About Us")
# Returns: {"section": "About Us", "success": True, "url_after": "..."}

# Navigate all sections
results = nav_page.navigate_all_sections(["About Us", "Services"])

# Validate navigation structure
validation = nav_page.validate_navigation_structure()
```

---

### Utility Classes

#### SoftAssertions
```python
soft_assert = SoftAssertions()

soft_assert.assert_true(condition, "Message")
soft_assert.assert_equal(actual, expected, "Message")
soft_assert.assert_in(item, collection, "Message")

# Continue testing even if assertions fail
soft_assert.print_failures()
if soft_assert.has_failures():
    # Handle failures
```

#### DataExtractor
```python
# Extract emails
emails = DataExtractor.extract_emails(text)

# Extract phones
phones = DataExtractor.extract_phone_numbers(text)

# Validate formats
is_valid_email = DataExtractor.validate_email(email)
is_valid_phone = DataExtractor.validate_phone(phone)
```

---

## 📊 Test Cases

### Test 1: Header Validation & Data Extraction
**Objective**: Extract and validate header information  
**Scope**:
- Page load validation
- Company name extraction
- Logo validation
- Email extraction and validation
- Phone extraction and validation
- Data persistence to JSON

### Test 2: Navigation Structure Analysis
**Objective**: Analyze website navigation dynamically  
**Scope**:
- Dynamically capture all menu items
- Identify dropdown menus
- Validate navigation structure
- Generate navigation map

### Test 3: Full Section Navigation
**Objective**: Navigate through all website sections  
**Scope**:
- Navigate to key sections (About Us, Services, Portfolio, Contact)
- Validate URL changes
- Validate page titles
- Generate navigation report

### Test 4: Complete Website Validation
**Objective**: End-to-end comprehensive validation  
**Scope**:
- Combines all three tests
- Header validation
- Navigation analysis
- Section navigation
- Final comprehensive report

---

## 📈 Reports and Artifacts

### Generated Outputs

```
reports/
├── header_data.json                    # Extracted header information
├── navigation_structure.json           # Menu items and dropdown structure
├── navigation_results.json             # Navigation test results
└── complete_validation_report.json     # Complete test report

screenshots/
├── header_highlighted_TIMESTAMP.png    # Highlighted header
├── AboutUs_TIMESTAMP.png               # About Us page
├── Services_TIMESTAMP.png              # Services page
└── ...

framework.log                           # Detailed test execution log

allure-results/                         # Allure report data
```

### JSON Report Structure

```json
{
  "website": "https://www.inheritx.com",
  "page_title": "...",
  "header_data": {
    "company_info": {
      "name": "InheritX",
      "logo_alt": "..."
    },
    "contact_info": {
      "emails": [...],
      "phones": [...]
    },
    "contact_validation": {
      "emails_valid": [...],
      "phones_valid": [...]
    }
  },
  "menu_items": [...],
  "navigation_results": [...]
}
```

---

## 🎯 Best Practices Implemented

### 1. **Modularity**
- Separate components for different functionalities
- Reusable page objects
- Common utility library

### 2. **Scalability**
- Dynamic element detection (not hardcoded)
- Flexible navigation handling
- Easy to extend for new sections

### 3. **Reliability**
- Comprehensive logging
- Soft assertions for non-blocking failures
- Explicit wait strategies
- Error screenshots on failure

### 4. **Maintainability**
- Centralized locators
- Configuration-driven tests
- Data extraction logic separation
- Clear method naming

### 5. **Observability**
- All actions logged with INFO level
- Warnings for soft assertion failures
- Screenshots for visual validation
- JSON exports for data analysis

---

## 🔍 Advanced Features

### Element Highlighting
```python
# Highlight element with red border
base_page.highlight_element("h1")

# Highlight and screenshot
base_page.highlight_and_screenshot("header", "header_section")
```

### Dynamic Waits
```python
# Wait for element with custom timeout
base_page.wait_for_element("nav", timeout=10000)

# Wait for page load state
base_page.wait_for_load_state('networkidle')
```

### Data Extraction
```python
# Extract multiple data types
emails = DataExtractor.extract_emails(page_text)
phones = DataExtractor.extract_phone_numbers(page_text)
structured = DataExtractor.structure_header_data(emails, phones, company)
```

### Soft Assertions
```python
# All assertions continue, collect failures
soft_assert.assert_equal(actual, expected, msg)
soft_assert.print_failures()
assert not soft_assert.has_failures()  # Fail test after all assertions
```

---

## 📝 Logging Strategy

### Log Levels Used

- **INFO**: Normal test flow, actions performed, assertions passed
- **WARNING**: Soft assertion failures, elements not found but non-critical
- **ERROR**: Critical failures, exceptions

### Log Output

```
2026-04-07 13:45:23,456 - INFO - Opening URL: https://www.inheritx.com
2026-04-07 13:45:24,789 - INFO - Header found. Highlighting...
2026-04-07 13:45:25,123 - INFO - Extracted 2 email(s): [...]
2026-04-07 13:46:01,456 - INFO - All navigation items captured successfully
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Tests timeout waiting for elements  
**Solution**: Check `TIMEOUT` value in `.env`, increase if needed

**Issue**: Navigation fails due to dynamic content  
**Solution**: Increase `wait_for_load_state` timeout in `navigate_to_section`

**Issue**: Allure report not generating  
**Solution**: Run `pip install allure-pytest` and use `--alluredir=allure-results`

**Issue**: Screenshots not saving  
**Solution**: Ensure `screenshots/` and `reports/` directories exist

---

## 🚀 Future Enhancements

- [ ] Cross-browser parallel execution
- [ ] Mobile viewport testing
- [ ] API integration layer
- [ ] Database assertions
- [ ] Performance metrics tracking
- [ ] CI/CD pipeline integration
- [ ] Custom reporting dashboard

---

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)

---

## ✅ Checklist

- [x] Base page with 30+ methods
- [x] Header component with data extraction
- [x] Navigation component with dynamic handling
- [x] Soft assertions library
- [x] Data extraction utilities
- [x] Comprehensive test suite (4 tests)
- [x] Logging and reporting
- [x] Screenshot capture with highlighting
- [x] JSON data export
- [x] Allure integration
- [x] Documentation

---

**Framework Status**: ✅ **Production Ready**  
**Last Updated**: April 7, 2026  
**Version**: 1.0.0
