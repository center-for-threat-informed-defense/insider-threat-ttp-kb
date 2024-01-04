Identifying and Mitigating Threats
==================================

The MITRE ATT&CK® framework has mapped data sources and mitigations, where applicable, to each of the techniques detailed in the ATT&CK® for Enterprise framework. These have been validated in terms of external actors, but the Center research team behind the Insider Threat Knowledge Base is validating these for their applicability to insider threats as well. The Center team is working under the assumption that many or most of the mitigations and data sources listed will help both efforts, but that there will likely be some differences or additional data sources and mitigations for insider threat.

Mitigations 
------------
Mitigations have been identified through their mappings to ATT&CK® TTPs and through validation by Center participants. Currently all insider threat TTPs within the Knowledge Base are also TTPs in ATT&CK®, therefore those ATT&CK® identified mitigations have been considered. Through discussion with participants, further mitigations may be identified in the future however as of the latest release, all mitigations for ATT&CK® for enterprise have been able to be identified as useful for insider threat as well. 
The chart below details the tactic, technique and mitigation mappings specific to insider threat. 


Data Sources
-------------
Identifying the most common data sources to detect insider threat will enhance the communities ability to prevent further threats. The data sources will be identified first through mappings from ATT&CK, like the mitigations. However, Center participants have identified and confirmed the data sources used for each detected TTP. 

.. tip::

   Select between the Mitigations and Data Sources tabs below to view their associated Insider Threat ATT&CK tactics and techniques.

.. raw:: html

   <!-- Tab links -->
   <div class="tab">
   <button class="tablinks" onclick="openTab(event, 'mitigations_fig')" id="defaultOpen">Mitigations</button>
   <button class="tablinks" onclick="openTab(event, 'datasources_fig')">Data Sources</button>
   </div>

   <!-- Tab content -->
   <div id="mitigations_fig" class="tabcontent">
      <h3>Mitigations</h3>
      <div class="tab-container">
         <iframe src="../_static/html/mitigations-1.html" height="1045px" width="100%"></iframe>
         <button class="btn btn-secondary btn-sm fullscreen-button" onclick="toggleFullscreen('mitigations_fig')">
                  <i class="fa fa-arrows-alt"></i>
                  Full Screen
         </button>
      </div>
   </div>

   <div id="datasources_fig" class="tabcontent">
      <h3>Data Sources</h3>
      <div class="tab-container">
         <iframe src="../_static/html/datasources-1.html" height="1045px" width="100%"></iframe>
         <button class="btn btn-secondary btn-sm fullscreen-button" onclick="toggleFullscreen('datasources_fig')">
                  <i class="fa fa-arrows-alt"></i>
                  Full Screen
         </button>
      </div>
   </div>

   <style>
      /* Style the tab */
      .tab {
      overflow: hidden;
      border: 1px solid #ccc;
      background-color: #f1f1f1;
      }

      /* Style the buttons that are used to open the tab content */
      .tab button {
      background-color: inherit;
      float: left;
      border: none;
      outline: none;
      cursor: pointer;
      padding: 14px 16px;
      transition: 0.3s;
      }

      /* Change background color of buttons on hover */
      .tab button:hover {
      background-color: #ddd;
      }

      /* Create an active/current tablink class */
      .tab button.active {
      background-color: #ccc;
      }

      /* Style the tab content */
      .tabcontent {
      display: none;
      padding: 6px 12px;
      border: 1px solid #ccc;
      border-top: none;
      }

      .fullscreen-button {
      position: absolute;
      bottom: 5px;
      right: 5px;
      }    

      .tab-container {
      position: relative;
      }

      @media all and (display-mode: fullscreen) {
      .container-container {
         display: flex;
         align-items: center;
         justify-content: center;
      }
   </style>

   <script>
      // Get the element with id="defaultOpen" and click on it
      document.getElementById("defaultOpen").click();

      function openTab(evt, tabName) {
         console.log("Calling openTab w tab name: " + tabName);
         // Declare all variables
         var i, tabcontent, tablinks;
         // Get all elements with class="tabcontent" and hide them
         tabcontent = document.querySelectorAll(".tabcontent");
         console.log("Hiding tabs: ")
         console.log(tabcontent);
         for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
         }
         // Get all elements with class="tablinks" and remove the class "active"
         tablinks = document.querySelectorAll(".tablinks");
         for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
         }
         // Show the current tab, and add an "active" class to the button that opened the tab
         document.querySelector(`#${tabName}`).style.display = "block";
         evt.currentTarget.className += " active";
      }

      function toggleFullscreen(elementName) {
         if (document.fullscreenElement) {
               document.exitFullscreen();
         } else {
               document.querySelector(`#${elementName} div`).requestFullscreen();
         }
      }
   </script>