#!/bin/bash

# 🚀 Quick Start Script for Playwright Framework
# This script sets up and runs the automation framework

echo "================================"
echo "  Playwright Framework Quick Start"
echo "================================"
echo ""

# Step 1: Install dependencies
echo "📦 Step 1: Installing Dependencies..."
pip install -r requirements.txt
playwright install
echo "✓ Dependencies installed"
echo ""

# Step 2: Verify installation
echo "🔍 Step 2: Verifying Installation..."
pytest --version
allure --version
echo "✓ Installation verified"
echo ""

# Step 3: Create directories
echo "📁 Step 3: Creating Output Directories..."
mkdir -p reports screenshots
echo "✓ Directories created"
echo ""

# Step 4: Run header validation test
echo "🧪 Step 4: Running Header Validation Test..."
pytest tests/test_login.py::TestInheritXFramework::test_header_validation_and_data_extraction -v --alluredir=allure-results
echo ""

# Step 5: Generate Allure report
echo "📊 Step 5: Generating Allure Report..."
echo "To view the report, run: allure serve allure-results"
echo ""

echo "✅ Quick Start Complete!"
echo ""
echo "📚 Next Steps:"
echo "  1. Read FRAMEWORK_GUIDE.md for detailed documentation"
echo "  2. Check IMPLEMENTATION_SUMMARY.md for feature overview"
echo "  3. Run: pytest tests/ -v  (for all tests)"
echo "  4. Run: allure serve allure-results  (to view report)"
echo ""
echo "Happy Testing! 🎉"
