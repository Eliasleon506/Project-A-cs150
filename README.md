# Air Pollution and the Thomas Fire: Data Visualization Project

**Author:** [Elias]  
**Course:** [Community Computing: CS-150 ]  


---

## **Thesis Statement**  
The Thomas Fire, one of California’s most destructive wildfires, significantly impacted air quality in the affected regions. This project visualizes changes in air pollution metrics such as AQI and PM2.5 levels during and after the wildfire, revealing the environmental consequences of such catastrophic events.

---

## **Context for the Data Visualization**  
Wildfires are increasingly frequent and severe due to climate change, and their impact on air quality poses serious public health risks. The Thomas Fire, which began on December 4, 2017, burned over 280,000 acres in Southern California. By visualizing air quality metrics before, during, and after the fire, we aim to tell a compelling story of how this environmental disaster affected the surrounding communities.

The visualization will focus on locations such as Santa Barbara, Ventura, and surrounding regions. The graph allows users to select specific locations and metrics (AQI or PM2.5) to explore how pollution levels fluctuated during this period.

---

## **Data Source**  
The data for this project comes from the **EPA Air Quality System (AQS)** dataset, which provides daily mean concentrations of PM2.5 and AQI values for multiple monitoring stations in Southern California.

Key columns used from the dataset:
- **Date**: The observation date for air quality readings.
- **Local Site Name**: The monitoring location name.
- **Daily Mean PM2.5 Concentration**: A measure of fine particulate matter in the air (measured in micrograms per cubic meter).
- **Daily AQI Value**: The Air Quality Index, a standardized scale representing overall air quality.

---

## **Visualization Strategies (SwD Principles)**  
This visualization employs principles from the book **Storytelling with Data (SwD)** by Cole Nussbaumer Knaflic to ensure effective storytelling:

1. **Choosing the Right Graph Type**  
   We use interactive line graphs to show trends in AQI and PM2.5 levels over time. This makes it easy to observe changes in air quality before, during, and after the Thomas Fire.

2. **Focus Attention with Annotations**  
   A vertical dotted line marks December 4, 2017, the date the Thomas Fire started. An annotation highlights this date as a key event, drawing the viewer’s attention to changes in air quality.

3. **Simplify for Clarity**  
   By providing dropdown filters for location and metric selection, users can explore specific subsets of the data without overwhelming the graph with excessive information.

4. **Color for Meaning**  
   Distinct colors are used to represent different locations, ensuring clear differentiation. The vertical line marking the fire’s start is in orange, symbolizing fire and urgency.

5. **Context and Comparisons**  
   Users can compare different locations and observe how air quality varied across regions during the same period, allowing for more meaningful insights.

---

By leveraging these strategies, the visualization aims to provide a compelling and educational story about the Thomas Fire’s impact on air quality and its broader environmental implications.

