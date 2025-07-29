# SQL for IoT Data Analysis - Professional Training Course

**Complete 9-week curriculum with custom-built learning tools for high school technical education**

A comprehensive educational program that teaches SQL fundamentals through practical IoT data analysis. This course represents a complete learning ecosystem with custom-developed simulators, structured curriculum, and progressive skill-building designed specifically for high school students entering the data analysis field.

## 🎯 Course Overview

This program transforms students from SQL beginners to competent data analysts capable of creating professional-grade dashboards using real IoT sensor data. The course emphasizes practical, hands-on learning through custom-built educational tools and industry-relevant datasets.

### **Key Achievement**: High school students successfully created professional Grafana dashboards by course completion.

## ✨ Complete Educational Solution

### **Custom-Built Learning Platform**
- **[SQL Simulator](https://github.com/jan-milacek/SQL_simulator)** - Python/Streamlit-based interactive SQL learning environment
- **[MQTT Dashboard](https://github.com/jan-milacek/mqtt_dashboard)** - Real-time IoT sensor data monitoring and simulation tool
- **Integrated curriculum** - Progressive exercises building from basic queries to complex analytics
- **No external dependencies** - Complete learning environment built from scratch

### **Professional-Grade Outcomes**
- Students master industry-standard SQL syntax and best practices
- Real-time data analysis using modern visualization tools (Grafana)
- Understanding of complete IoT data pipeline from collection to visualization
- Portfolio-ready projects demonstrating practical data analysis skills

## 🏗️ Course Architecture

```
Complete Learning Ecosystem
├── Week 1-5: SQL Fundamentals
│   ├── Custom SQL Simulator
│   ├── Progressive exercises
│   ├── Real IoT datasets
│   └── Error-friendly learning environment
├── Week 6-7: Data Visualization  
│   ├── SQL-based chart creation
│   ├── Export and sharing capabilities
│   └── Visual storytelling with data
├── Week 8-9: Professional Dashboards
│   ├── Grafana integration
│   ├── Real-time monitoring setup
│   ├── Interactive dashboard creation
│   └── Professional presentation skills
└── Supporting Tools
    ├── MQTT data simulation
    ├── Real-time sensor monitoring
    ├── Microsoft Teams integration
    └── Assignment tracking system
```

## 📚 Detailed Curriculum

### **Week 1-2: Database Fundamentals**
**Learning Objectives:**
- Understand relational database concepts
- Master basic SELECT statements
- Learn proper WHERE clause usage
- Practice data filtering and sorting

**Tools & Activities:**
- Introduction to SQL Simulator interface
- IoT sensor data exploration exercises
- Basic query writing with immediate feedback
- Error analysis and debugging practice

**Practical Exercises:**
```sql
-- Week 1: Basic data exploration
SELECT * FROM senzory WHERE typ = 'temperature';

-- Week 2: Data filtering
SELECT nazev_senzoru, umisteni 
FROM senzory 
WHERE datum_instalace > '2023-01-01'
ORDER BY nazev_senzoru;
```

### **Week 3: Aggregation and Grouping**
**Learning Objectives:**
- Master aggregate functions (COUNT, AVG, SUM, MIN, MAX)
- Understand GROUP BY and HAVING clauses
- Analyze sensor data patterns
- Create summary statistics

**Practical Exercises:**
```sql
-- Sensor performance analysis
SELECT typ, COUNT(*) as sensor_count, 
       AVG(hodnota) as avg_reading
FROM mereni m 
JOIN senzory s ON m.sensor_id = s.sensor_id
GROUP BY typ
HAVING COUNT(*) > 100;
```

### **Week 4: Table Relationships and JOINs**
**Learning Objectives:**
- Understand relational database design
- Master INNER, LEFT, and RIGHT JOINs
- Combine sensor metadata with measurements
- Create comprehensive data views

**Practical Exercises:**
```sql
-- Complete sensor analysis with location data
SELECT s.umisteni, s.nazev_senzoru, 
       COUNT(m.mereni_id) as reading_count,
       MIN(m.casova_znamka) as first_reading,
       MAX(m.casova_znamka) as last_reading
FROM senzory s
LEFT JOIN mereni m ON s.sensor_id = m.sensor_id
GROUP BY s.sensor_id, s.umisteni, s.nazev_senzoru;
```

### **Week 5: Time-Series Analysis**
**Learning Objectives:**
- Master date and time functions
- Analyze temporal patterns in IoT data
- Create time-based aggregations
- Understand data seasonality

**Practical Exercises:**
```sql
-- Daily temperature trends
SELECT DATE(casova_znamka) as day,
       HOUR(casova_znamka) as hour,
       AVG(hodnota) as avg_temp,
       MIN(hodnota) as min_temp,
       MAX(hodnota) as max_temp
FROM mereni m
JOIN senzory s ON m.sensor_id = s.sensor_id
WHERE s.typ = 'temperature'
  AND casova_znamka >= DATE_SUB(NOW(), INTERVAL 7 DAY)
GROUP BY DATE(casova_znamka), HOUR(casova_znamka)
ORDER BY day, hour;
```

### **Week 6-7: Data Visualization and Reporting**
**Learning Objectives:**
- Create charts directly from SQL queries
- Design effective data visualizations
- Export and share analytical results
- Build visual narratives with data

**Tools & Activities:**
- SQL Simulator visualization features
- Chart type selection for different data types
- Interactive chart configuration
- Export to various formats (PNG, HTML, CSV)

**Practical Projects:**
- Sensor performance comparison charts
- Time-series trend analysis visualizations
- Geographic distribution of sensor readings
- Statistical distribution analysis

### **Week 8-9: Professional Dashboard Creation**
**Learning Objectives:**
- Set up and configure Grafana
- Connect SQL data sources to visualization tools
- Create interactive, real-time dashboards
- Design professional presentations of data insights

**Tools & Activities:**
- Grafana installation and configuration
- MQTT Dashboard for real-time data simulation
- Professional dashboard design principles
- Stakeholder presentation skills

**Capstone Project:**
Students create a complete IoT monitoring dashboard featuring:
- Real-time sensor data display
- Historical trend analysis
- Alerting for abnormal readings
- Professional styling and layout
- Presentation to class stakeholders

## 🛠️ Custom Educational Tools

### **SQL Simulator Features**
```python
# Built with Python/Streamlit
# Key capabilities:
- Multi-CSV data loading
- In-memory SQLite database
- Real-time query execution
- Error handling and explanations
- Interactive visualization
- Results export functionality
```

### **MQTT Dashboard Features**
```python
# Real-time IoT simulation
# Key capabilities:
- MQTT broker integration
- Sensor data simulation
- Real-time monitoring
- Message publishing
- Data persistence
- Educational sensor scenarios
```

### **Integrated Learning Environment**
- **Microsoft Teams integration** - Assignment tracking and communication
- **Progressive difficulty** - Carefully sequenced skill building
- **Error-friendly design** - Helpful error messages and debugging support
- **Real datasets** - Industry-relevant IoT sensor data
- **Professional tools** - Same technologies used in production environments

## 🎓 Learning Outcomes & Assessment

### **Technical Skills Achieved**
- **SQL Proficiency**: Students write complex analytical queries independently
- **Data Visualization**: Create professional charts and dashboards
- **Time-Series Analysis**: Understand temporal patterns and seasonality
- **Database Design**: Comprehend relational data structures
- **Tool Integration**: Connect multiple technologies in complete workflows

### **Professional Skills Developed**
- **Problem-solving**: Debug queries and resolve data quality issues
- **Communication**: Present data insights to technical and non-technical audiences
- **Project management**: Complete multi-week technical projects
- **Critical thinking**: Evaluate data quality and analytical approaches
- **Industry readiness**: Use production-grade tools and methodologies

### **Assessment Methods**
- **Weekly assignments** - Progressive skill-building exercises
- **Practical projects** - Real-world data analysis challenges
- **Peer collaboration** - Team-based problem solving
- **Capstone presentation** - Professional dashboard demonstration
- **Portfolio development** - Collection of completed projects

## 📊 Course Effectiveness Metrics

### **Student Success Indicators**
- **100% completion rate** in pilot implementation
- **Professional-quality outputs** - Grafana dashboards indistinguishable from industry work
- **Skill progression** - From zero SQL knowledge to complex analytical queries
- **Engagement levels** - High participation and voluntary project extensions
- **Career readiness** - Students prepared for entry-level data analysis roles

### **Educational Innovation**
- **Custom tool development** - No existing educational platforms met course requirements
- **Practical application focus** - Real IoT datasets instead of academic examples
- **Industry alignment** - Tools and techniques used in professional environments
- **Progressive complexity** - Carefully designed learning progression
- **Student-centered design** - Built specifically for teenage learners

## 🚀 Implementation Guide

### **For Educational Institutions**

**Technical Requirements:**
- Computer lab with modern web browsers
- Local network for MQTT broker setup
- Python 3.7+ for tool deployment
- Basic IT support for initial setup

**Instructor Preparation:**
- Familiarity with basic SQL concepts
- Understanding of IoT fundamentals
- Comfort with Python/Streamlit applications
- Grafana basic configuration knowledge

**Course Deployment:**
```bash
# Setup for classroom use
git clone https://github.com/jan-milacek/SQL_simulator.git
git clone https://github.com/jan-milacek/mqtt_dashboard.git

# Install dependencies
pip install streamlit pandas sqlite3 paho-mqtt plotly

# Launch applications
streamlit run SQL_simulator/app.py
streamlit run mqtt_dashboard/mqtt_dashboard.py
```

### **Adaptation Guidelines**
- **Duration flexibility** - Adapt from 9 weeks to semester-length or intensive formats
- **Skill level adjustment** - Modify complexity for different student backgrounds
- **Industry focus** - Customize datasets for local industries (manufacturing, agriculture, healthcare)
- **Language localization** - Translate interface and materials for non-English speakers

## 🤝 Contributing to Course Development

### **Areas for Enhancement**
- **Additional industry datasets** - Manufacturing, healthcare, agriculture sensor data
- **Extended curriculum modules** - Advanced analytics, machine learning integration
- **Assessment automation** - Automatic query evaluation and feedback
- **Mobile compatibility** - Tablet and smartphone interface optimization
- **Collaboration features** - Team-based project tools

### **Community Contributions**
- **Translated materials** - Course content in multiple languages
- **Industry partnerships** - Real-world case studies and guest experts
- **Technology updates** - Integration with latest data tools and platforms
- **Pedagogical research** - Effectiveness studies and improvement recommendations

## 📞 Support & Implementation

### **For Educators**
- **Setup assistance** - Technical guidance for course deployment
- **Curriculum customization** - Adapt content for specific institutional needs
- **Instructor training** - Workshops for effective course delivery
- **Assessment tools** - Rubrics and evaluation frameworks

### **For Students**
- **Self-paced learning** - Tools designed for independent study
- **Portfolio building** - Project templates for career preparation
- **Career guidance** - Pathways to data analysis and IoT careers
- **Continuing education** - Advanced course recommendations

### **Contact Information**
- **Course Creator**: Jan Miláček (jan.milacek@gmail.com)
- **Technical Support**: Create issues in respective tool repositories
- **Educational Partnerships**: Contact for institutional implementation
- **Community Discussion**: Join educational technology forums

## 🔗 Related Resources

### **Course Tools**
- [SQL Simulator Repository](https://github.com/jan-milacek/SQL_simulator) - Interactive SQL learning platform
- [MQTT Dashboard Repository](https://github.com/jan-milacek/mqtt_dashboard) - IoT data monitoring and simulation

### **Professional Development**
- **Data Engineering Career Paths** - Industry role progression
- **Certification Recommendations** - Professional credentials in data analysis
- **Industry Connections** - Internship and job placement resources
- **Continuing Education** - Advanced courses and specialization options

## 📜 License & Usage

**Educational Use License (MIT-based)**
- ✅ **Free for educational institutions** - Non-commercial classroom use
- ✅ **Modification encouraged** - Adapt for local needs and requirements
- ✅ **Attribution required** - Credit original course development
- ✅ **Commercial training** - Contact for licensing commercial implementations

## 🎯 Impact & Recognition

### **Educational Achievement**
This course represents a significant achievement in technical education:

- **Custom tool development** - Built complete learning platform from scratch
- **Student success** - High school students achieving professional-level skills
- **Industry relevance** - Direct alignment with data analysis career requirements
- **Pedagogical innovation** - Novel approach to teaching complex technical concepts
- **Scalable solution** - Replicable model for other institutions

### **Professional Validation**
- **Open source availability** - Community validation and contribution
- **Real-world applicability** - Skills directly transferable to employment
- **Tool sophistication** - Professional-grade educational technology
- **Comprehensive scope** - Complete curriculum with supporting infrastructure
- **Measurable outcomes** - Demonstrable student skill acquisition

---

**Built with ❤️ for the next generation of data professionals**

*This course demonstrates that complex technical concepts can be made accessible through thoughtful curriculum design, custom tool development, and student-centered pedagogy. The combination of practical application with professional-grade tools creates a powerful educational experience that prepares students for real-world data analysis challenges.*
