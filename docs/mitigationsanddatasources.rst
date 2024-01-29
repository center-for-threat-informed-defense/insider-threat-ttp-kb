Identifying and Mitigating Threats
==================================

The MITRE ATT&CK® framework has mapped data sources and mitigations, where applicable, to each of the techniques detailed in the ATT&CK® for Enterprise framework. These have been validated in terms of external actors, but the Center research team behind the Insider Threat Knowledge Base is validating these for their applicability to insider threats as well. The Center team is working under the assumption that many or most of the mitigations and data sources listed will help both efforts, but that there will likely be some differences or additional data sources and mitigations for insider threat.

Mitigations 
------------
Mitigations have been identified through their mappings to ATT&CK® TTPs and through validation by Center participants. Currently all insider threat TTPs within the Knowledge Base are also TTPs in ATT&CK®, therefore those ATT&CK® identified mitigations have been considered. Through discussion with participants, further mitigations may be identified in the future however as of the latest release, all mitigations for ATT&CK® for enterprise have been able to be identified as useful for insider threat as well. 
The chart below details the tactic, technique and mitigation mappings specific to insider threat. 

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="..\mitigations.csv" download="mitigations.csv">
        <i class="fa fa-download"></i> Download Table CSV 6KB</a>
    </p>

.. csv-table:: Techniques and Mitigations
   :file: /extra/mitigations.csv
   :header-rows: 1

Data Sources
-------------
Data sources that are useful for providing relevant information for insider threat identification have been detailed. Identifying the most common data sources to detect insider threat will enhance the communities' ability to mitigate insider threat. The data sources have been identified first through mappings from ATT&CK®, like the mitigations, with follow-on confirmation from Center participants. 
The chart below details the tactic, technique and data source mappings specific to insider threat. 

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="..\datasources.csv" download="datasources.csv">
        <i class="fa fa-download"></i> Download Table CSV 7KB</a>
    </p>

.. csv-table:: Techniques and Data Sources
   :file: /extra/datasources.csv
   :header-rows: 1

.. tip::

   Select between the Mitigations and Data Sources tabs below to view insider threat techniques with their corresponding mitigations.
.. .. raw:: html

   .. <script src="https://cdn.plot.ly/plotly-latest.min.js"></script> 

.. .. raw:: html

..    <!-- Tab links -->
..    <div class="tab">
..    <button class="tablinks" onclick="openTab(event, 'mitigations_fig')" id="defaultOpen">Mitigations</button>
..    <button class="tablinks" onclick="openTab(event, 'datasources_fig')">Data Sources</button>
..    </div>

..    <!-- Tab content -->
..    <div id="mitigations_fig" class="tabcontent">
..       <h3>Mitigations</h3>
..       <div class="tab-container">
..          <iframe src="../_static/html/mitigations-1.html" height="1145px" width="100%"></iframe>
..          <button class="btn btn-secondary btn-sm fullscreen-button" onclick="toggleFullscreen('mitigations_fig')">
..                   <i class="fa fa-arrows-alt"></i>
..                   Full Screen
..          </button>
..       </div>
..    </div>

..    <div id="datasources_fig" class="tabcontent">
..       <h3>Data Sources</h3>
..       <div class="tab-container">
..          <iframe src="../_static/html/datasources-1.html" height="1145px" width="100%"></iframe>
..          <button class="btn btn-secondary btn-sm fullscreen-button" onclick="toggleFullscreen('datasources_fig')">
..                   <i class="fa fa-arrows-alt"></i>
..                   Full Screen
..          </button>
..       </div>
..    </div>

..    <style>
..       /* Style the tab */
..       .tab {
..       overflow: hidden;
..       border: 1px solid #ccc;
..       background-color: #f1f1f1;
..       }

..       /* Style the buttons that are used to open the tab content */
..       .tab button {
..       background-color: inherit;
..       float: left;
..       border: none;
..       outline: none;
..       cursor: pointer;
..       padding: 14px 16px;
..       transition: 0.3s;
..       color: var(--me-hyperlink)
..       }

..       /* Change background color of buttons on hover */
..       .tab button:hover {
..       background-color: #ddd;
..       color: var(--me-text-color)
..       }

..       /* Create an active/current tablink class */
..       .tab button.active {
..       background-color: #ccc;
..       }

..       /* Style the tab content */
..       .tabcontent {
..       display: none;
..       padding: 6px 12px;
..       border: 1px solid #ccc;
..       border-top: none;
..       }

..       path:hover {
..       fill: gold !important;
..       fill-opacity: 1 !important;
..       }

..       .sankey-link:hover {
..       fill: gold !important;
..       fill-opacity: 1 !important;
..       }

..       .fullscreen-button {
..       position: absolute;
..       bottom: 5px;
..       right: 5px;
..       }    

..       .tab-container {
..       position: relative;
..       }

..       @media all and (display-mode: fullscreen) {
..          .container-container {
..             display: flex;
..             align-items: center;
..             justify-content: center;
..          }

..          .tab-container iframe {
..             height: 100%;
..          }
..       }
..    </style>

..    <script>
..       // Get the element with id="defaultOpen" and click on it
..       document.getElementById("defaultOpen").click();

..       function openTab(evt, tabName) {
..          console.log("Calling openTab w tab name: " + tabName);
..          // Declare all variables
..          var i, tabcontent, tablinks;
..          // Get all elements with class="tabcontent" and hide them
..          tabcontent = document.querySelectorAll(".tabcontent");
..          console.log("Hiding tabs: ")
..          console.log(tabcontent);
..          for (i = 0; i < tabcontent.length; i++) {
..             tabcontent[i].style.display = "none";
..          }
..          // Get all elements with class="tablinks" and remove the class "active"
..          tablinks = document.querySelectorAll(".tablinks");
..          for (i = 0; i < tablinks.length; i++) {
..             tablinks[i].className = tablinks[i].className.replace(" active", "");
..          }
..          // Show the current tab, and add an "active" class to the button that opened the tab
..          document.querySelector(`#${tabName}`).style.display = "block";
..          evt.currentTarget.className += " active";
..       }

..       function toggleFullscreen(elementName) {
..          if (document.fullscreenElement) {
..                document.exitFullscreen();
..                document.querySelector(`#${elementName} div`).style.width = "100%";
..          } else {
..                let element = document.querySelector(`#${elementName} div`);
..                element.requestFullscreen();
..                element.style.width = "50%";
..          }
..       }
..    </script>
