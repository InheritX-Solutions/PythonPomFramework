import re
import json
from utils.logger import get_logger

logger = get_logger()


class DataExtractor:
    """Extract and validate business data from web pages"""

    @staticmethod
    def extract_emails(text):
        """Extract all email addresses from text"""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(pattern, text)
        logger.info(f"Extracted {len(emails)} email(s): {emails}")
        return emails

    @staticmethod
    def extract_phone_numbers(text):
        """Extract phone numbers from text"""
        pattern = r'\+?[\d\s\-\(\)]{7,}'
        phones = re.findall(pattern, text)
        logger.info(f"Extracted {len(phones)} phone number(s): {phones}")
        return phones

    @staticmethod
    def validate_email(email):
        """Validate email format"""
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        is_valid = bool(re.match(pattern, email))
        logger.info(f"Email '{email}' validation: {is_valid}")
        return is_valid

    @staticmethod
    def validate_phone(phone):
        """Validate phone number format"""
        # Remove all non-digit characters except +
        cleaned = re.sub(r'[^\d+]', '', phone)
        # Check if it has minimum 7 digits
        is_valid = len(re.findall(r'\d', cleaned)) >= 7
        logger.info(f"Phone '{phone}' validation: {is_valid}")
        return is_valid

    @staticmethod
    def extract_links(page, locator):
        """Extract all links from elements matching locator"""
        try:
            links = page.locator(locator).get_attribute("href")
            logger.info(f"Extracted link: {links}")
            return links
        except:
            logger.warning(f"Failed to extract link from {locator}")
            return None

    @staticmethod
    def structure_header_data(emails, phones, company_name):
        """Structure extracted header data"""
        data = {
            "company_name": company_name,
            "emails": {
                "valid": [e for e in emails if DataExtractor.validate_email(e)],
                "invalid": [e for e in emails if not DataExtractor.validate_email(e)]
            },
            "phones": {
                "valid": [p for p in phones if DataExtractor.validate_phone(p)],
                "invalid": [p for p in phones if not DataExtractor.validate_phone(p)]
            }
        }
        logger.info(f"Structured header data: {json.dumps(data, indent=2)}")
        return data

    @staticmethod
    def extract_navigation_items(page, nav_locator):
        """Extract all navigation menu items"""
        items = page.locator(nav_locator).all_text_contents()
        items = [item.strip() for item in items if item.strip()]
        logger.info(f"Extracted navigation items: {items}")
        return items

    @staticmethod
    def structure_navigation_data(menu_items, dropdowns):
        """Structure navigation data with dropdown information"""
        data = {
            "total_items": len(menu_items),
            "menu_items": menu_items,
            "dropdowns": dropdowns,
            "non_dropdown_items": [item for item in menu_items if item not in [d["name"] for d in dropdowns]]
        }
        logger.info(f"Structured navigation data: {json.dumps(data, indent=2)}")
        return data

    @staticmethod
    def save_to_json(data, filename):
        """Save extracted data to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data to {filename}: {str(e)}")
            return False
