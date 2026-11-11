from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.dml import MSO_THEME_COLOR

OUT = 'NEXORA_Member2_Viva_Presentation.pptx'
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

BG = RGBColor(9, 16, 30)
PANEL = RGBColor(20, 32, 52)
CYAN = RGBColor(0, 220, 235)
BLUE = RGBColor(76, 165, 255)
GREEN = RGBColor(0, 220, 130)
AMBER = RGBColor(255, 184, 70)
WHITE = RGBColor(242, 247, 252)
MUTED = RGBColor(166, 183, 202)
RED = RGBColor(255, 93, 121)


def set_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG
    # accent line
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.16), prs.slide_height)
    shape.fill.solid(); shape.fill.fore_color.rgb = CYAN; shape.line.fill.background()


def textbox(slide, text, x, y, w, h, size=20, color=WHITE, bold=False, align=PP_ALIGN.LEFT, font='Aptos'):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame; tf.clear(); tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.name = font; run.font.size = Pt(size); run.font.bold = bold; run.font.color.rgb = color
    return box


def title(slide, heading, sub=''):
    textbox(slide, heading, 0.65, 0.42, 12.0, 0.55, 28, WHITE, True, font='Aptos Display')
    if sub: textbox(slide, sub, 0.68, 1.02, 11.8, 0.35, 12, MUTED)


def footer(slide, n):
    textbox(slide, f'NEXORA  |  Member 2: Backend & Database  |  {n}', 0.68, 7.12, 12, 0.2, 9, MUTED)


def bullet_box(slide, items, x, y, w, h, accent=CYAN, size=17):
    panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    panel.fill.solid(); panel.fill.fore_color.rgb = PANEL; panel.line.color.rgb = RGBColor(42, 62, 88)
    tf = panel.text_frame; tf.clear(); tf.margin_left = Inches(0.25); tf.margin_right = Inches(0.18); tf.margin_top = Inches(0.18)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = '- ' + item; p.level = 0; p.font.name = 'Aptos'; p.font.size = Pt(size); p.font.color.rgb = WHITE; p.space_after = Pt(10)
    # accent bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(0.08), Inches(h))
    bar.fill.solid(); bar.fill.fore_color.rgb = accent; bar.line.fill.background()
    return panel


def card(slide, label, value, x, y, w, h, accent=CYAN):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid(); shape.fill.fore_color.rgb = PANEL; shape.line.color.rgb = RGBColor(42, 62, 88)
    textbox(slide, label.upper(), x+0.2, y+0.18, w-0.4, 0.25, 10, MUTED, True)
    textbox(slide, value, x+0.2, y+0.55, w-0.4, h-0.65, 19, accent, True)


def arrow(slide, x1, y1, x2, y2, color=CYAN):
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    line.line.color.rgb = color; line.line.width = Pt(2.5)

# 1
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s)
textbox(s, 'NEXORA', 0.9, 1.25, 11.5, 0.8, 48, CYAN, True, PP_ALIGN.CENTER, 'Aptos Display')
textbox(s, 'AI-Powered Stock Market Prediction Dashboard', 1.0, 2.15, 11.3, 0.5, 25, WHITE, True, PP_ALIGN.CENTER)
textbox(s, 'Viva Voce Presentation', 1.0, 2.85, 11.3, 0.35, 16, MUTED, False, PP_ALIGN.CENTER)
card(s, 'Presented by', 'Member 2', 4.0, 4.25, 2.2, 1.2, GREEN)
card(s, 'Module', 'Backend & Database', 6.45, 4.25, 2.9, 1.2, BLUE)
textbox(s, 'PHP  |  Flask  |  MySQL  |  Python ML  |  REST APIs', 1.0, 6.35, 11.3, 0.3, 14, MUTED, False, PP_ALIGN.CENTER)

# 2
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'Project Overview', 'A centralized platform for stock analysis and educational forecasting')
bullet_box(s, ['Users register and securely log in.', 'Stocks can be searched, selected, and added to a watchlist.', 'Historical prices and technical indicators are visualized.', 'An ML service produces future price estimates.', 'User data and prediction history are stored in MySQL.'], 0.85, 1.55, 6.0, 4.65, CYAN, 18)
card(s, 'Main goal', 'Convert complex market data into understandable user information', 7.35, 1.75, 4.9, 1.55, GREEN)
card(s, 'My focus', 'Backend integration, database persistence, authentication, and APIs', 7.35, 3.65, 4.9, 1.55, BLUE)
textbox(s, 'The backend is the communication layer between the frontend, database, and prediction engine.', 7.55, 5.65, 4.5, 0.7, 16, WHITE, True)
footer(s, 2)

# 3
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'Problem Statement and Solution')
textbox(s, 'PROBLEM', 0.9, 1.5, 5.3, 0.35, 14, RED, True)
bullet_box(s, ['Stock information is spread across multiple sources.', 'Raw financial data is difficult for beginners to interpret.', 'Users need secure storage for watchlists and predictions.', 'Frontend and ML services need a reliable connection.'], 0.85, 1.92, 5.6, 3.8, RED, 17)
textbox(s, 'SOLUTION', 7.0, 1.5, 5.3, 0.35, 14, GREEN, True)
bullet_box(s, ['NEXORA combines analysis and prediction in one system.', 'PHP APIs connect the interface with MySQL and Flask.', 'MySQL stores user-specific application records.', 'JSON responses update the dashboard dynamically.'], 6.95, 1.92, 5.6, 3.8, GREEN, 17)
footer(s, 3)

# 4 architecture
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'System Architecture', 'How the main components communicate')
labels = [('Browser / Frontend', 0.8, 2.55, CYAN), ('PHP Application\n& API Proxy', 3.45, 2.55, BLUE), ('MySQL\nDatabase', 6.1, 2.55, GREEN), ('Flask REST API\nPython ML', 8.75, 2.55, AMBER), ('Prediction\nEngine', 11.0, 2.55, RED)]
for text, x, y, c in labels:
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(1.8), Inches(1.15))
    sh.fill.solid(); sh.fill.fore_color.rgb = PANEL; sh.line.color.rgb = c; sh.line.width = Pt(2)
    textbox(s, text, x+0.1, y+0.28, 1.6, 0.55, 15, WHITE, True, PP_ALIGN.CENTER)
for x in [2.62, 5.27, 7.92, 10.67]: arrow(s, x, 3.12, x+0.78, 3.12)
textbox(s, 'Requests', 1.1, 4.3, 2.0, 0.3, 13, MUTED, False, PP_ALIGN.CENTER)
textbox(s, 'SQL + JSON', 3.7, 4.3, 2.0, 0.3, 13, MUTED, False, PP_ALIGN.CENTER)
textbox(s, 'Prediction request', 8.55, 4.3, 2.3, 0.3, 13, MUTED, False, PP_ALIGN.CENTER)
textbox(s, 'The PHP layer centralizes validation, database access, and communication with the Flask service.', 1.35, 5.65, 10.7, 0.55, 19, WHITE, True, PP_ALIGN.CENTER)
footer(s, 4)

# 5 contribution
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'Member 2 Responsibilities')
items = [('Flask backend', 'Expose prediction functionality through REST APIs', CYAN), ('MySQL database', 'Design tables and relationships for persistent records', GREEN), ('Authentication', 'Register users, verify passwords, and manage sessions', BLUE), ('Prediction history', 'Save model outputs and evaluation metrics per user', AMBER), ('Integration', 'Connect frontend requests with backend and ML responses', RED)]
for i, (head, desc, c) in enumerate(items):
    x = 0.85 + (i % 3) * 4.15; y = 1.6 + (i // 3) * 2.2
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.6), Inches(1.55))
    sh.fill.solid(); sh.fill.fore_color.rgb = PANEL; sh.line.color.rgb = c
    textbox(s, head, x+0.22, y+0.22, 3.1, 0.32, 18, c, True)
    textbox(s, desc, x+0.22, y+0.7, 3.1, 0.55, 14, WHITE)
textbox(s, 'My contribution makes the application connected, persistent, and user-specific.', 1.3, 6.15, 10.7, 0.4, 20, WHITE, True, PP_ALIGN.CENTER)
footer(s, 5)

# 6 auth
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'User Registration and Login', 'Authentication protects personal records and private dashboard pages')
steps = [('1', 'Register', 'Validate details and create user record'), ('2', 'Hash password', 'Store only a secure password hash'), ('3', 'Login', 'Find user and verify password'), ('4', 'Create session', 'Store user ID for protected requests')]
for i, (num, head, desc) in enumerate(steps):
    x = 0.8 + i*3.1
    sh = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x+1.05), Inches(1.65), Inches(0.75), Inches(0.75))
    sh.fill.solid(); sh.fill.fore_color.rgb = [CYAN, BLUE, GREEN, AMBER][i]; sh.line.fill.background()
    textbox(s, num, x+1.05, 1.82, 0.75, 0.3, 18, BG, True, PP_ALIGN.CENTER)
    textbox(s, head, x, 2.7, 2.9, 0.35, 18, WHITE, True, PP_ALIGN.CENTER)
    textbox(s, desc, x+0.1, 3.25, 2.7, 0.8, 14, MUTED, False, PP_ALIGN.CENTER)
    if i < 3: arrow(s, x+2.15, 2.02, x+3.0, 2.02, MUTED)
bullet_box(s, ['Prepared statements reduce SQL injection risk.', 'password_hash() and password_verify() protect credentials.', 'require_login() prevents access to private pages.'], 2.2, 4.65, 8.9, 1.45, BLUE, 16)
footer(s, 6)

# 7 database
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'MySQL Database Design', 'Relational storage for users, market records, and application activity')
tables = [('users', 'accounts, password hashes, preferences', CYAN), ('stocks', 'symbols and company names', BLUE), ('stock_history', 'OHLCV historical records', GREEN), ('watchlist', 'user-stock tracking relationship', AMBER), ('predictions', 'forecast values and metrics', RED), ('prediction_history', 'saved prediction references', CYAN)]
for i, (name, desc, c) in enumerate(tables):
    x = 0.85 + (i%3)*4.15; y = 1.55 + (i//3)*2.1
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.55), Inches(1.35))
    sh.fill.solid(); sh.fill.fore_color.rgb = PANEL; sh.line.color.rgb = c
    textbox(s, name, x+0.2, y+0.2, 3.1, 0.3, 18, c, True)
    textbox(s, desc, x+0.2, y+0.65, 3.1, 0.4, 14, WHITE)
textbox(s, 'User ID links personal records such as watchlists, portfolios, and predictions.', 1.25, 6.05, 10.8, 0.4, 18, WHITE, True, PP_ALIGN.CENTER)
footer(s, 7)

# 8 api
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'API and Frontend Integration', 'The frontend communicates with PHP using HTTP requests and JSON')
endpoints = [('quote', 'Current quote and OHLCV values'), ('details', 'Historical series and stock metadata'), ('movers', 'Top gainers and losers'), ('predict', 'Forecast and model metrics')]
for i, (name, desc) in enumerate(endpoints):
    y = 1.45 + i*1.05
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(y), Inches(2.0), Inches(0.65))
    sh.fill.solid(); sh.fill.fore_color.rgb = BLUE; sh.line.fill.background()
    textbox(s, name, 1.1, y+0.18, 1.8, 0.25, 16, BG, True, PP_ALIGN.CENTER)
    arrow(s, 3.15, y+0.32, 4.0, y+0.32, CYAN)
    textbox(s, desc, 4.25, y+0.12, 4.2, 0.35, 16, WHITE, True)
textbox(s, 'JSON response', 9.0, 2.55, 2.3, 0.35, 18, GREEN, True, PP_ALIGN.CENTER)
textbox(s, '{ status: success, symbol, current_price, prediction, metrics }', 8.0, 3.1, 4.3, 1.0, 15, MUTED, False, PP_ALIGN.CENTER, 'Consolas')
bullet_box(s, ['Fetch API avoids full-page reloads.', 'The proxy manages Flask communication and fallback behavior.', 'The frontend updates cards and charts from the response.'], 8.0, 4.65, 4.3, 1.5, GREEN, 15)
footer(s, 8)

# 9 prediction
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'Prediction History Workflow', 'How a forecast becomes a user-specific database record')
steps = [('Request', 'User selects ticker'), ('Process', 'Flask model returns forecast'), ('Display', 'PHP returns JSON to UI'), ('Save', 'User submits prediction'), ('History', 'Record stored in MySQL')]
for i, (head, desc) in enumerate(steps):
    x = 0.75 + i*2.5
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(2.0), Inches(1.95), Inches(1.15))
    sh.fill.solid(); sh.fill.fore_color.rgb = PANEL; sh.line.color.rgb = [CYAN, BLUE, GREEN, AMBER, RED][i]
    textbox(s, head, x+0.1, 2.22, 1.75, 0.25, 16, [CYAN, BLUE, GREEN, AMBER, RED][i], True, PP_ALIGN.CENTER)
    textbox(s, desc, x+0.12, 2.62, 1.7, 0.35, 12, WHITE, False, PP_ALIGN.CENTER)
    if i < 4: arrow(s, x+1.98, 2.58, x+2.43, 2.58, MUTED)
bullet_box(s, ['Stored fields include symbol, current price, predicted price, change percentage, target date, RMSE, MAE, MAPE, and model version.', 'Prediction history is filtered by the logged-in user ID.'], 1.45, 4.55, 10.3, 1.35, AMBER, 17)
footer(s, 9)

# 10 security and limitations
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'Security, Reliability, and Limitations')
bullet_box(s, ['Prepared SQL statements', 'Password hashing and verification', 'Session-based page protection', 'Input normalization and HTML escaping', 'User-specific database queries'], 0.85, 1.5, 5.7, 4.5, GREEN, 17)
bullet_box(s, ['Some historical data is simulated in the prototype.', 'Prediction values from hidden form fields need stronger server validation.', 'Prediction accuracy is not yet compared with actual future prices.', 'Production deployment should use verified live market data.'], 6.85, 1.5, 5.7, 4.5, AMBER, 17)
textbox(s, 'These limitations identify clear future development work rather than affecting the core architecture.', 1.4, 6.25, 10.5, 0.35, 17, WHITE, True, PP_ALIGN.CENTER)
footer(s, 10)

# 11 conclusion
s = prs.slides.add_slide(prs.slide_layouts[6]); set_bg(s); title(s, 'Conclusion', 'Suggested viva closing statement')
textbox(s, '“My work developed the backend and database foundation of NEXORA. The system authenticates users, stores their records securely, processes stock requests, communicates with the Flask prediction service, and returns structured JSON data to the frontend. MySQL provides persistent storage for users, watchlists, portfolios, and prediction history. Overall, this module makes the dashboard connected, reliable, and user-specific. Future improvements include verified live market data, stronger validation, and automatic prediction accuracy tracking.”', 1.2, 1.65, 10.9, 3.15, 23, WHITE, False, PP_ALIGN.CENTER)
card(s, 'Key message', 'Backend + Database = reliable system integration', 4.15, 5.45, 5.0, 1.1, CYAN)
footer(s, 11)

prs.save(OUT)
print(OUT)
