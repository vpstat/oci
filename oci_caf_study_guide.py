import streamlit as st


# Page configuration
st.set_page_config(
    page_title="OCI Cloud Adoption Framework Study Guide",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for book-like appearance
st.markdown("""
    <style>
    .main {
        background-color: #f5f5dc;
    }
    .stMarkdown {
        font-family: 'Georgia', serif;
    }
    h1 {
        color: #c74634;
        border-bottom: 3px solid #c74634;
        padding-bottom: 10px;
    }
    h2 {
        color: #312509;
        border-left: 5px solid #c74634;
        padding-left: 15px;
        margin-top: 30px;
    }
    h3 {
        color: #4a4a4a;
        font-style: italic;
    }
    .highlight-box {
        background-color: #fff8dc;
        border-left: 5px solid #ffa500;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .key-concept {
        background-color: #e6f3ff;
        border-left: 5px solid #0066cc;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .exam-tip {
        background-color: #fff0f0;
        border-left: 5px solid #ff0000;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Table of Contents")
st.sidebar.markdown("---")

chapters = {
    "Introduction": "intro",
    "OCI Core Concepts": "core_concepts",
    "OCI 2025 Exam Topics": "exam_topics",
    "1. Business Strategy": "business",
    "2. People Strategy": "people",
    "3. Security (Shared Model)": "security",
    "4. Process Design": "process",
    "5. Technology Implementation": "tech",
    "6. Management & Operations": "mgmt",
    "Quick Reference": "quick_ref"
}

selected_chapter = st.sidebar.radio("Navigate to:", list(chapters.keys()))

# Main content area
if selected_chapter == "Introduction":
    st.title("☁️ Oracle Cloud Infrastructure Cloud Adoption Framework")
    st.markdown("### *A Comprehensive Study Guide for OCI Certification*")
    
    st.markdown("---")
    
    st.markdown("""
    ## What is the OCI Cloud Adoption Framework?
    
    The **Oracle Cloud Infrastructure (OCI) Cloud Adoption Framework (CAF)** is a structured methodology that provides 
    best practices and prescriptive guidance for organizations to successfully adopt cloud technologies.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>🎯 Key Purpose</h3>
    Cloud adoption empowers organizations to:
    <ul>
        <li>Improve business agility</li>
        <li>Promote innovative solutions</li>
        <li>Transform through phased approach</li>
        <li>Leverage experience-based recommendations for people, processes, and technology</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## The Six Pillars of Success")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 1. 📊 Business Strategy
        Define and communicate business goals for cloud adoption
        
        ### 2. 👥 People Strategy
        Formalize Cloud Center of Excellence (CCOE) and workforce readiness
        
        ### 3. 🔒 Security
        Define foundational security aspects and shared responsibility model
        """)
    
    with col2:
        st.markdown("""
        ### 4. ⚙️ Process Design
        Identify business and technical processes for cloud adoption
        
        ### 5. 🛠️ Technology Implementation
        Transform processes into a secure landing zone environment
        
        ### 6. 📈 Management & Operations
        Keep cloud environment running smoothly post-deployment
        """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tip</h3>
    <strong>Remember:</strong> Cloud adoption is <strong>multilayered</strong> and extends beyond technology implementation. 
    It requires organization-wide change management, executive support, clear business goals, workforce readiness, 
    and modernization of business and IT processes.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## Framework Approach
    
    - **Complete Story**: The framework is presented as a complete, standardized approach
    - **Adaptable**: Organizations should adapt based on their unique needs
    - **Independent Pillars**: Can follow recommendations in each pillar independently
    - **Iterative**: Take an iterative approach as priorities change and strategy evolves
    """)

elif selected_chapter == "OCI Core Concepts":
    st.title("🏗️ OCI Core Concepts")
    st.markdown("### *Understanding Oracle Cloud Infrastructure Fundamentals*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    Before diving into the Cloud Adoption Framework, it's essential to understand the foundational components 
    of Oracle Cloud Infrastructure (OCI). These concepts form the building blocks for all cloud deployments.
    """)
    
    st.markdown("## Physical Architecture Concepts")
    
    st.markdown("### 🌍 Regions")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is a Region?</h4>
    A <strong>Region</strong> is a localized geographic area containing one or more data centers (availability domains).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Regions are **independent** of other regions
    - Can be separated by vast distances (across countries or continents)
    - Generally, deploy applications in the region where they're most heavily used
    - Using nearby resources is faster than using distant resources
    
    **Why Deploy in Different Regions?**
    - **Risk Mitigation**: Protect against region-wide events (weather systems, earthquakes)
    - **Compliance**: Meet legal jurisdictions, tax domains requirements
    - **Business Criteria**: Address social and business requirements
    
    **Realms:**
    - Regions are grouped into **realms**
    - Your tenancy exists in a **single realm**
    - Can access all regions in your realm
    - **Cannot** access regions outside your realm
    - Types: Commercial, Government, Dedicated
    """)
    
    st.markdown("### 🏢 Availability Domains (ADs)")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is an Availability Domain?</h4>
    An <strong>Availability Domain</strong> is one or more data centers located within a region.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Availability domains within the same region are connected by **low latency, high bandwidth network**
    - Enables high-availability connectivity to internet and on-premises
    - Build replicated systems across multiple ADs for HA and DR
    - Oracle randomizes ADs by tenancy to balance capacity
    
    **Naming Convention:**
    - Tenancy-specific prefixes (e.g., `Uocm:PHX-AD-1`, `Uocm:PHX-AD-2`)
    - Same AD name in different tenancies may refer to different data centers
    - Use `ListAvailabilityDomains` API to get your tenancy's specific AD names
    
    **Important Notes:**
    - New regions may launch with **one availability domain**
    - Expansion options: add capacity to existing ADs, add new ADs, or build new region
    - Based on customer requirements and regional demand patterns
    """)
    
    st.markdown("### ⚡ Fault Domains")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is a Fault Domain?</h4>
    A <strong>Fault Domain</strong> is a grouping of hardware and infrastructure within an availability domain.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Each availability domain contains **three fault domains**
    - Provide **anti-affinity** placement
    - Hardware failure in one fault domain doesn't affect instances in other fault domains
    - Compute maintenance events are isolated to single fault domain
    
    **Use Cases:**
    - Protect against unexpected hardware failures
    - Protect against planned outages due to Compute hardware maintenance
    
    **Placement Control:**
    - Optionally specify fault domain at instance launch
    - If not specified, system selects one automatically
    - OCI makes best-effort anti-affinity placement
    - Can edit fault domain for compute instances
    - For DB systems: terminate and relaunch in preferred fault domain
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>💡 High Availability Strategy</h4>
    <strong>Best Practice:</strong> Distribute instances across multiple fault domains within an availability domain, 
    and across multiple availability domains within a region for maximum resilience.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Account and Access Concepts")
    
    st.markdown("### 🏛️ Tenancy")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is a Tenancy?</h4>
    A <strong>Tenancy</strong> is the root compartment that holds all your cloud resources.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Represents your entire Oracle Cloud account
    - Exists in a single realm
    - Has a unique Oracle Cloud Identifier (OCID)
    - All resources belong to the tenancy
    
    **Tenancy Limits:**
    - **Trial/Free Tier/Pay-as-you-go**: Limited to one subscribed region
    - **Pay-as-you-go**: Can request limit increase
    - **Universal Monthly Credit**: Can subscribe to all publicly released commercial regions
    """)
    
    st.markdown("### 📁 Compartments")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is a Compartment?</h4>
    A <strong>Compartment</strong> is a logical container for organizing and isolating cloud resources.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Organize resources by project, department, or environment
    - Control access through IAM policies
    - Resources can be moved between compartments
    - Hierarchical structure (compartments within compartments)
    - Simplify resource management and billing
    
    **Best Practices:**
    - Create compartments for different teams or projects
    - Use for cost tracking and access control
    - Implement least-privilege access model
    """)
    
    st.markdown("### 🔐 Identity Domains and Policies")
    
    st.markdown("""
    **Identity and Access Management (IAM):**
    - Control who can access which resources
    - Define **policies** that specify permissions
    - Use **identity domains** to manage users and groups
    
    **IAM Policies:**
    - Written in simple policy language
    - Grant access to specific resources in specific compartments
    - Support principle of least privilege
    - Can be attached to compartments or tenancy
    
    **Example Policy Statement:**
    ```
    Allow group ProjectA-Developers to manage instances in compartment ProjectA
    ```
    """)
    
    st.markdown("### 🆔 Oracle Cloud Identifier (OCID)")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is an OCID?</h4>
    An <strong>OCID</strong> is a unique identifier assigned to every Oracle Cloud resource.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Globally unique across all of Oracle Cloud
    - Used in API calls and CLI commands
    - Format includes resource type and region information
    - Immutable (doesn't change for the lifetime of the resource)
    
    **Example OCID:**
    ```
    ocid1.instance.oc1.phx.abyhqljt...
    ```
    """)
    
    st.markdown("### 🛡️ Security Zones")
    
    st.markdown("""
    **Security Zones** enforce security best practices automatically:
    - Prevent common security misconfigurations
    - Ensure resources comply with security policies
    - Block actions that would violate security posture
    - Provide additional layer of protection
    
    **Examples of Enforced Policies:**
    - Prevent creation of public buckets
    - Require encryption for block volumes
    - Enforce network security rules
    """)
    
    st.markdown("---")
    
    st.markdown("## Core Services Concepts")
    
    st.markdown("### 🌐 Virtual Cloud Network (VCN)")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is a VCN?</h4>
    A <strong>Virtual Cloud Network (VCN)</strong> is a customizable, private network in Oracle Cloud Infrastructure.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Software-defined network in OCI
    - Resides in a single region
    - Can span multiple availability domains
    - Define your own IP address space (CIDR blocks)
    - Create subnets, route tables, and gateways
    
    **VCN Components:**
    - **Subnets**: Subdivisions of VCN (can be public or private)
    - **Route Tables**: Control traffic routing
    - **Security Lists**: Virtual firewall rules
    - **Internet Gateway**: Access to/from internet
    - **NAT Gateway**: Outbound internet access for private subnets
    - **Service Gateway**: Access to Oracle services without internet
    - **Dynamic Routing Gateway (DRG)**: Connect to on-premises network
    
    **Common Scenarios:**
    - **Scenario A**: Public subnet (web servers)
    - **Scenario B**: Private subnet with VPN (database servers)
    - **Scenario C**: Public and private subnets with VPN (multi-tier app)
    """)
    
    st.markdown("### 💻 Compute Instances")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is an Instance?</h4>
    An <strong>Instance</strong> is a virtual machine (VM) or bare metal server running in OCI.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Choose from various **shapes** (CPU, memory configurations)
    - Select **platform images** (Oracle Linux, Ubuntu, Windows, etc.)
    - Or use custom images
    - Attached to VCN via Virtual Network Interface Card (VNIC)
    
    **Instance Types:**
    - **Virtual Machines (VMs)**: Shared hardware, flexible sizing
    - **Bare Metal**: Dedicated physical servers, maximum performance
    - **Dedicated Virtual Machine Hosts**: VMs on dedicated hardware
    
    **Compute Shapes:**
    - **Standard**: Balanced CPU and memory
    - **Dense I/O**: High local storage
    - **GPU**: Graphics processing
    - **High Performance Computing (HPC)**: Cluster networking
    - **Flexible**: Customize CPU and memory independently
    """)
    
    st.markdown("### 💾 Block Volumes")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is a Block Volume?</h4>
    A <strong>Block Volume</strong> is network-attached storage that persists beyond the life of an instance.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Characteristics:**
    - Persistent and durable storage
    - Independent of compute instances
    - Can be attached/detached from instances
    - Automatically replicated for high durability
    - Encrypted at rest and in transit
    
    **Use Cases:**
    - Expand instance storage capacity
    - Persistent data storage
    - Move data between instances
    - Create backups and clones
    
    **Performance Tiers:**
    - **Lower Cost**: For infrequent access
    - **Balanced**: General purpose workloads
    - **Higher Performance**: I/O intensive applications
    - **Ultra High Performance**: Extreme performance needs
    
    **Volume Features:**
    - **Backups**: Manual or automatic scheduled backups
    - **Clones**: Fast, space-efficient copies
    - **Volume Groups**: Manage multiple volumes together
    - **Cross-Region Replication**: DR and data migration
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🔗 How Components Work Together</h4>
    <strong>Typical Architecture:</strong>
    <ol>
        <li><strong>Region</strong> contains your resources</li>
        <li><strong>Tenancy</strong> is your root container</li>
        <li><strong>Compartments</strong> organize resources by project/team</li>
        <li><strong>VCN</strong> provides networking in an availability domain</li>
        <li><strong>Subnets</strong> within VCN host your instances</li>
        <li><strong>Instances</strong> run your applications</li>
        <li><strong>Block Volumes</strong> provide persistent storage</li>
        <li><strong>Fault Domains</strong> ensure high availability</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚖️ Load Balancing")
    
    st.markdown("""
    <div class="key-concept">
    <h4>What is Load Balancing?</h4>
    A <strong>Load Balancer</strong> provides automated traffic distribution from one entry point to multiple servers 
    reachable from your VCN.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Benefits:**
    - **Improved Resource Utilization**: Distribute workload across multiple servers
    - **Facilitates Scaling**: Easily add or remove backend servers
    - **High Availability**: Ensures service continuity even if servers fail
    - **Health Monitoring**: Automatically detects and routes around unhealthy instances
    - **Maintenance Window Reduction**: Drain traffic before removing servers for maintenance
    
    **Load Balancer Features:**
    - Choice of **public** or **private** IP address
    - **Provisioned bandwidth** based on shape
    - **SSL handling** for incoming and backend traffic
    - Multiple **load balancing policies**
    - Application-specific **health checks**
    - **Session persistence** options
    """)
    
    st.markdown("#### Load Balancer Types")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Public Load Balancer:**
        - Has a **public IP address**
        - Accessible from the internet
        - Requires **two subnets** in different ADs
        - Ensures high availability
        - Active in only one subnet at a time
        - Automatically fails over to second subnet
        
        **Use Cases:**
        - Web applications
        - Public-facing APIs
        - Internet-accessible services
        """)
    
    with col2:
        st.markdown("""
        **Private Load Balancer:**
        - Has a **private IP address**
        - Only accessible within VCN
        - Requires **one subnet**
        - Internal traffic distribution
        - Not exposed to internet
        
        **Use Cases:**
        - Internal applications
        - Database tier load balancing
        - Microservices communication
        - Backend API services
        """)
    
    st.markdown("#### Load Balancer Components")
    
    st.markdown("""
    **1. Backend Set:**
    - Collection of backend servers
    - Defines load balancing policy
    - Includes health check configuration
    - Can have multiple backend sets per load balancer
    
    **2. Backend Servers:**
    - Actual compute instances receiving traffic
    - Added to backend sets
    - Can be in different availability domains
    - Weighted for traffic distribution
    
    **3. Listener:**
    - Monitors for incoming traffic
    - Configured with protocol and port
    - Routes traffic to backend set
    - Can handle SSL termination
    
    **4. Health Check:**
    - Monitors backend server health
    - Protocol: HTTP, HTTPS, TCP
    - Configurable interval and timeout
    - Automatically removes unhealthy servers from rotation
    """)
    
    st.markdown("#### Load Balancing Policies")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>Traffic Distribution Policies</h4>
    The policy determines how traffic is distributed to backend servers:
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Round Robin:**
    - Distributes traffic **sequentially** to each server
    - When all servers receive a connection, repeats the list
    - Simple and effective for similar server capacities
    - Default policy for most use cases
    
    **Weighted Round Robin:**
    - Similar to Round Robin but with **weights**
    - Servers with higher weights receive more traffic
    - Useful when servers have different capacities
    
    **IP Hash:**
    - Uses source IP address as **hashing key**
    - Routes requests from same client to same backend server
    - Maintains session affinity without cookies
    - As long as server is available
    
    **Least Connections:**
    - Routes traffic to server with **fewest active connections**
    - Balances load based on current server utilization
    - Good for long-lived connections
    - Prevents overloading busy servers
    """)
    
    st.markdown("#### Load Balancer Shapes")
    
    st.markdown("""
    **Shapes determine bandwidth:**
    - **10 Mbps**: Small applications, testing
    - **100 Mbps**: Small to medium applications
    - **400 Mbps**: Medium applications
    - **8 Gbps**: Large applications
    - **Flexible**: Custom bandwidth (10 Mbps to 8 Gbps)
    
    **Important Notes:**
    - Shape **cannot be changed** after creation
    - Choose based on expected traffic
    - Bandwidth is provisioned and guaranteed
    - All shapes come with same features
    """)
    
    st.markdown("#### Configuration Steps")
    
    st.markdown("""
    **To create a functional load balancer:**
    
    1. **Create Load Balancer**
       - Choose shape (bandwidth)
       - Select VCN
       - Choose visibility (public/private)
       - Select subnets (2 for public, 1 for private)
    
    2. **Create Backend Set**
       - Define name
       - Select load balancing policy
       - Configure health check (protocol, port, URL path)
    
    3. **Add Backend Servers**
       - Select compute instances
       - Specify port
       - Set weight (for weighted policies)
    
    4. **Create Listener**
       - Define name
       - Select protocol (HTTP, HTTPS, TCP)
       - Specify port (e.g., 80 for HTTP, 443 for HTTPS)
       - Associate with backend set
    
    5. **Update Security Lists**
       - Allow incoming traffic to listener port
       - Allow traffic from load balancer to backend servers
       - Configure appropriate security rules
    
    6. **Verify Configuration**
       - Check health status of backend servers
       - Test load balancer public IP
       - Verify traffic distribution
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>💡 Load Balancer Best Practices</h4>
    <ul>
        <li><strong>High Availability</strong>: Use public load balancer with two subnets in different ADs</li>
        <li><strong>Health Checks</strong>: Configure appropriate health check intervals and thresholds</li>
        <li><strong>Security</strong>: Use SSL/TLS for sensitive data, configure proper security lists</li>
        <li><strong>Monitoring</strong>: Enable logging and monitor metrics for performance</li>
        <li><strong>Session Persistence</strong>: Use when application requires sticky sessions</li>
        <li><strong>Backend Protection</strong>: Place backend servers in private subnets</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


elif selected_chapter == "OCI 2025 Exam Topics":
    st.title("🎓 OCI 2025 Architect Associate Exam Topics")
    st.markdown("### *Comprehensive Coverage of Certification Topics*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    This chapter covers all topics from the **Oracle Cloud Infrastructure 2025 Architect Associate** certification exam.
    Each section includes key concepts, configuration details, and references to official Oracle documentation.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h4>📋 Exam Topic Areas</h4>
    <ul>
        <li><strong>Compute:</strong> Instances, Autoscaling, Images, OS Management</li>
        <li><strong>Networking:</strong> VCN, Connectivity, DNS, Load Balancing, Network Command Center</li>
        <li><strong>Storage:</strong> Block, Object, and File Storage</li>
        <li><strong>Identity & Access Management:</strong> IAM Policies, Dynamic Groups, Access Control</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Compute Section
    st.markdown("## 💻 Compute")
    st.markdown("---")
    
    st.markdown("### Select Appropriate Compute Choices")
    
    st.markdown("""
    **Compute Shapes:**
    - **Standard Shapes:** Balanced CPU and memory for general workloads
    - **Dense I/O Shapes:** High local NVMe SSD storage for big data
    - **GPU Shapes:** Graphics processing for AI/ML, rendering
    - **HPC Shapes:** High-performance computing with cluster networking
    - **Flexible Shapes:** Customize CPU and memory independently
    - **Optimized Shapes:** Optimized for specific workloads (AMD, Intel)
    
    **Instance Types:**
    - **Virtual Machines (VMs):** Shared hardware, cost-effective
    - **Bare Metal:** Dedicated physical servers, maximum performance
    - **Dedicated Virtual Machine Hosts:** VMs on dedicated hardware for licensing
    
    **Selection Criteria:**
    - Workload requirements (CPU, memory, storage, network)
    - Performance needs
    - Cost considerations
    - Licensing requirements
    
    📚 **Reference:** [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)
    """)
    
    st.markdown("### Configure Compute Instances")
    
    st.markdown("""
    **Launch Configuration:**
    - Select compartment and availability domain
    - Choose shape and image
    - Configure networking (VCN, subnet, public IP)
    - Add SSH keys for access
    - Configure boot volume size
    - Add cloud-init scripts (optional)
    
    **Instance Management:**
    - **Start/Stop/Reboot:** Control instance state
    - **Terminate:** Delete instance (preserves boot volume optionally)
    - **Console Connection:** Access via VNC for troubleshooting
    - **Instance Metadata:** Access instance information
    - **Custom Metadata:** Add key-value pairs
    
    **Advanced Options:**
    - **Fault Domain:** Specify for high availability
    - **Capacity Reservation:** Reserve capacity in advance
    - **Preemptible Instances:** Low-cost, interruptible instances
    
    📚 **Reference:** [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)
    """)
    
    st.markdown("### Configure Autoscaling")
    
    st.markdown("""
    **Instance Pools:**
    - Collection of identical instances
    - Span multiple availability domains for HA
    - Use instance configuration as template
    - Attach to load balancer backend set
    
    **Autoscaling Configuration:**
    - **Metric-Based:** Scale based on CPU, memory utilization
    - **Schedule-Based:** Scale at specific times
    - **Scaling Policies:**
      - Scale-out threshold (add instances)
      - Scale-in threshold (remove instances)
      - Cooldown period between scaling actions
    
    **Configuration Steps:**
    1. Create instance configuration
    2. Create instance pool
    3. Create autoscaling configuration
    4. Define scaling policies
    5. Attach to load balancer (optional)
    
    📚 **Reference:** [Autoscaling](https://docs.oracle.com/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
    """)
    
    st.markdown("### OCI Compute Image Options")
    
    st.markdown("""
    **Platform Images:**
    - Oracle Linux (multiple versions)
    - CentOS, Ubuntu, Windows Server
    - Regularly updated by Oracle
    - Pre-configured and optimized for OCI
    
    **Custom Images:**
    - Create from existing instance
    - Import from on-premises
    - Share across compartments or tenancies
    - Export to Object Storage
    
    **Bring Your Own Image (BYOI):**
    - Import custom OS images
    - Must meet OCI requirements
    - Supports Linux and Windows
    
    **Image Management:**
    - **OCID:** Unique identifier for each image
    - **Compatibility:** Check shape compatibility
    - **Versioning:** Maintain multiple image versions
    
    📚 **Reference:** [Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm)
    """)
    
    st.markdown("### OS Management")
    
    st.markdown("""
    **OS Management Service:**
    - Centralized patch management
    - Package management
    - Compliance reporting
    - Automated patching schedules
    
    **Key Features:**
    - **Managed Instance Groups:** Group instances for management
    - **Scheduled Jobs:** Automate patching and updates
    - **Package Management:** Install, update, remove packages
    - **Compliance:** Track patch compliance
    
    **Configuration:**
    1. Enable OS Management Service Agent
    2. Create managed instance groups
    3. Define scheduled jobs
    4. Monitor compliance and status
    
    📚 **Reference:** [OS Management](https://docs.oracle.com/iaas/os-management/index.html)
    """)
    
    st.markdown("### Infrastructure Maintenance")
    
    st.markdown("""
    **Live Migration:**
    - **Transparent:** No downtime for most maintenance
    - **Automatic:** OCI handles migration
    - **Supported:** Most VM shapes (not bare metal)
    
    **Maintenance Events:**
    - **Scheduled Maintenance:** Planned infrastructure updates
    - **Notification:** Advance notice via email/console
    - **Reboot Migration:** Some events require reboot
    
    **Best Practices:**
    - **Fault Domains:** Distribute across multiple fault domains
    - **Availability Domains:** Use multiple ADs for critical workloads
    - **Monitoring:** Set up alerts for maintenance events
    - **Testing:** Test applications for migration compatibility
    
    📚 **Reference:** [Infrastructure Maintenance](https://docs.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm)
    """)
    
    # Networking Section
    st.markdown("## 🌐 Networking")
    st.markdown("---")
    
    st.markdown("### Implement and Manage Virtual Cloud Networks")
    
    st.markdown("""
    **VCN Fundamentals:**
    - Software-defined network in OCI
    - Regional resource (spans all ADs in region)
    - CIDR block: /16 to /30
    - Multiple subnets per VCN
    
    **Public vs Private Subnets:**
    
    **Public Subnet:**
    - Resources have public IP addresses
    - Direct internet access via Internet Gateway
    - Use for web servers, bastion hosts
    - Security: Restrict via Security Lists/NSGs
    
    **Private Subnet:**
    - No public IP addresses
    - Internet access via NAT Gateway (outbound only)
    - Use for databases, application servers
    - More secure, isolated from internet
    
    **IP Addresses:**
    - **Private IP:** Assigned to VNIC, internal communication
    - **Public IP:**
      - **Ephemeral:** Temporary, released when instance stops
      - **Reserved:** Persistent, can be reassigned
    
    **Virtual NICs (VNICs):**
    - Attached to instances
    - Primary VNIC (required) + Secondary VNICs (optional)
    - Each VNIC has private IP, optional public IP
    - Can attach to different subnets
    
    📚 **Reference:** [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm)
    """)
    
    st.markdown("### VCN Routing and Gateways")
    
    st.markdown("""
    **Route Tables:**
    - Define traffic routing rules
    - Associated with subnets
    - Rules specify destination CIDR and target
    
    **Gateways:**
    
    **Internet Gateway (IGW):**
    - Enables internet access for public subnets
    - Bidirectional traffic
    - One per VCN
    
    **NAT Gateway:**
    - Outbound-only internet access for private subnets
    - Prevents inbound connections
    - Blocks IP addresses if needed
    
    **Service Gateway (SGW):**
    - Access Oracle Services without internet
    - Traffic stays on Oracle network
    - Supports Object Storage, Autonomous Database
    
    **Dynamic Routing Gateway (DRG):**
    - Connect VCN to on-premises network
    - VCN peering (local and remote)
    - Multiple VCN attachments
    - Transit routing hub
    
    📚 **Reference:** [VCN Gateways](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm)
    """)
    
    st.markdown("### Security Lists and Network Security Groups")
    
    st.markdown("""
    **Security Lists:**
    - Virtual firewall rules for subnets
    - Stateful (return traffic automatically allowed)
    - Ingress and egress rules
    - Applied at subnet level
    - All resources in subnet inherit rules
    
    **Network Security Groups (NSGs):**
    - Virtual firewall for specific resources
    - More granular than Security Lists
    - Can reference other NSGs in rules
    - Applied to VNICs
    - Better for complex environments
    
    **Comparison:**
    | Feature | Security Lists | NSGs |
    |---------|---------------|------|
    | Scope | Subnet-level | Resource-level |
    | Granularity | Coarse | Fine |
    | Rule References | CIDR only | CIDR or NSG |
    | Best For | Simple setups | Complex environments |
    
    📚 **Reference:** [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)
    """)
    
    st.markdown("### VCN Connectivity Options")
    
    st.markdown("""
    **Site-to-Site VPN:**
    - IPSec VPN connection to on-premises
    - Encrypted tunnel over internet
    - Up to 250 Mbps per tunnel
    - Multiple tunnels for redundancy
    - Configuration: CPE (Customer-Premises Equipment) + DRG
    
    **FastConnect:**
    - Dedicated private connection
    - Higher bandwidth (1 Gbps to 10 Gbps)
    - Lower latency than VPN
    - More reliable and secure
    - Options: Colocation, Partner, Third-party
    
    **Local Peering:**
    - Connect VCNs in same region
    - Uses Local Peering Gateway (LPG)
    - Private IP communication
    - No internet traversal
    
    **Remote Peering:**
    - Connect VCNs across regions
    - Uses DRG
    - Encrypted over Oracle backbone
    - No internet traversal
    
    **Transit Routing:**
    - Hub-and-spoke topology
    - Central VCN routes traffic
    - Connect multiple VCNs and on-premises
    - Use DRG as transit hub
    
    📚 **Reference:** [VCN Connectivity](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm)
    """)
    
    st.markdown("### DNS and Traffic Management")
    
    st.markdown("""
    **DNS Zones:**
    
    **Public DNS:**
    - Publicly resolvable domain names
    - Hosted on Oracle's global DNS network
    - Supports standard DNS record types
    - High availability and performance
    
    **Private DNS:**
    - Internal name resolution within VCN
    - Not accessible from internet
    - Integrated with VCN
    - Custom domain names for private resources
    
    **Traffic Management:**
    - Intelligent DNS-based traffic steering
    - Global load balancing
    - Failover and disaster recovery
    
    **Steering Policies:**
    - **Load Balancer:** Distribute across multiple endpoints
    - **Failover:** Automatic failover to backup
    - **Geolocation:** Route based on user location
    - **ASN:** Route based on autonomous system number
    - **IP Prefix:** Route based on source IP
    
    📚 **Reference:** [DNS and Traffic Management](https://docs.oracle.com/iaas/Content/DNS/home.htm)
    """)
    
    st.markdown("### Load Balancer Concepts")
    
    st.markdown("""
    **Load Balancer:**
    - Layer 7 (HTTP/HTTPS) load balancing
    - SSL termination
    - Session persistence
    - Content-based routing
    - Shapes: 10 Mbps to 8 Gbps
    
    **Network Load Balancer:**
    - Layer 4 (TCP/UDP) load balancing
    - Ultra-low latency
    - High throughput (millions of requests/sec)
    - Preserves source IP
    - Flexible shapes
    
    **Components:**
    - **Backend Set:** Group of servers
    - **Backend Servers:** Actual compute instances
    - **Listener:** Monitors incoming traffic
    - **Health Check:** Monitors server health
    
    **Policies:**
    - Round Robin
    - Weighted Round Robin
    - IP Hash
    - Least Connections
    
    📚 **Reference:** [Load Balancing](https://docs.oracle.com/iaas/Content/Balance/home.htm)
    """)
    
    st.markdown("### Web Application Acceleration")
    
    st.markdown("""
    **Web Application Firewall (WAF):**
    - Protects web applications
    - OWASP Top 10 protection
    - DDoS mitigation
    - Bot management
    - Rate limiting
    
    **CDN (Content Delivery Network):**
    - Global content caching
    - Reduced latency
    - Improved performance
    - Integrated with Object Storage
    
    📚 **Reference:** [WAF](https://docs.oracle.com/iaas/Content/WAF/home.htm)
    """)
    
    st.markdown("### Network Command Center Services")
    
    st.markdown("""
    **Inter-Region Latency:**
    - Measure latency between OCI regions
    - Plan multi-region deployments
    - Optimize region selection
    
    **Network Visualizer:**
    - Visual topology of VCN resources
    - Interactive diagrams
    - Understand network architecture
    - Export diagrams
    
    **Network Path Analyzer:**
    - Troubleshoot connectivity issues
    - Analyze network paths
    - Identify routing problems
    - Test connectivity between resources
    
    **Virtual Test Access Points (VTAPs):**
    - Capture and inspect network traffic
    - Mirror traffic to analysis tools
    - Security monitoring
    - Troubleshooting
    
    **Capture Filters:**
    - Define what traffic to capture
    - Source/destination IP, port, protocol
    - VNIC-level filtering
    
    📚 **Reference:** [Network Command Center](https://docs.oracle.com/iaas/Content/Network/Concepts/network_command_center.htm)
    """)
    
    # Storage Section
    st.markdown("## 💾 Storage")
    st.markdown("---")
    
    st.markdown("### Block Storage")
    
    st.markdown("""
    **Performance Tiers:**
    - **Lower Cost:** 2 IOPS/GB, throughput 240 KB/s per GB
    - **Balanced:** 60 IOPS/GB, throughput 480 KB/s per GB
    - **Higher Performance:** 75 IOPS/GB, throughput 600 KB/s per GB
    - **Ultra High Performance:** 225 IOPS/GB, throughput 2,400 KB/s per GB
    
    **Block Volumes:**
    - Network-attached storage
    - Persistent, durable
    - Encrypted at rest and in transit
    - Attach/detach from instances
    - Size: 50 GB to 32 TB
    
    **Boot Volumes:**
    - Contains OS and boot data
    - Created automatically with instance
    - Can be detached and attached
    - Custom boot volume sizes
    
    **Volume Groups:**
    - Manage multiple volumes together
    - Consistent backups across volumes
    - Clone entire group
    
    **Backups:**
    - **Manual:** On-demand backups
    - **Scheduled:** Automatic policy-based
    - **Incremental:** Only changed blocks
    - **Cross-region:** Copy to other regions
    
    **Clones:**
    - Fast, space-efficient copies
    - Point-in-time copy
    - Independent from source
    
    **Cross-Region Replication:**
    - Asynchronous replication
    - Disaster recovery
    - Data migration
    
    📚 **Reference:** [Block Volume](https://docs.oracle.com/iaas/Content/Block/home.htm)
    """)
    
    st.markdown("### Object Storage")
    
    st.markdown("""
    **Storage Tiers:**
    
    **Standard:**
    - Hot data, frequent access
    - Immediate retrieval
    - Highest cost per GB
    
    **Infrequent Access:**
    - Warm data, occasional access
    - Immediate retrieval
    - Lower cost than Standard
    - Retrieval fees apply
    
    **Archive:**
    - Cold data, rare access
    - Must restore before access (1 hour)
    - Lowest cost per GB
    - Retrieval fees apply
    
    **Security:**
    - **Encryption:** At rest (AES-256), in transit (TLS)
    - **Pre-Authenticated Requests:** Time-limited URLs
    - **IAM Policies:** Fine-grained access control
    - **Bucket Policies:** Resource-level permissions
    
    **Versioning:**
    - Keep multiple versions of objects
    - Protect against accidental deletion
    - Restore previous versions
    
    **Lifecycle Management:**
    - Automatic tier transitions
    - Delete old objects
    - Archive infrequently accessed data
    
    **Retention Rules:**
    - Prevent deletion for specified period
    - Compliance and regulatory requirements
    - Time-based or indefinite
    
    **Multipart Uploads:**
    - Upload large objects in parts
    - Parallel uploads for speed
    - Resume failed uploads
    - Recommended for objects > 100 MB
    
    **Object Storage Replication:**
    - Replicate buckets across regions
    - Disaster recovery
    - Data locality
    
    📚 **Reference:** [Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)
    """)
    
    st.markdown("### File Storage")
    
    st.markdown("""
    **File Storage Service:**
    - NFS-based shared file system
    - Accessible from multiple instances
    - POSIX-compliant
    - Scalable and durable
    
    **Configuration:**
    - Create File System
    - Create Mount Target (in subnet)
    - Export Path
    - Mount from instances (NFS mount)
    
    **Security:**
    - **Encryption:** At rest and in transit
    - **Export Options:** Control access per client
    - **Security Lists/NSGs:** Network-level security
    - **IAM Policies:** Management access control
    
    **Snapshots:**
    - Point-in-time copies
    - Read-only
    - Space-efficient
    - Restore files or entire file system
    
    **Clones:**
    - Writable copy of file system
    - Based on snapshot
    - Independent from source
    
    **Usage and Metering:**
    - Monitor file system usage
    - Capacity and IOPS metrics
    - Billing based on usage
    
    **File Storage Replication:**
    - Replicate to another region
    - Disaster recovery
    - Asynchronous replication
    
    📚 **Reference:** [File Storage](https://docs.oracle.com/iaas/Content/File/home.htm)
    """)
    
    # IAM Section
    st.markdown("## 🔐 Identity and Access Management")
    st.markdown("---")
    
    st.markdown("### IAM Core Concepts")
    
    st.markdown("""
    **Identity and Access Management (IAM):**
    - Control who can access which resources
    - Authentication and authorization
    - Fine-grained access control
    
    **Key Components:**
    - **Users:** Individual people or applications
    - **Groups:** Collections of users
    - **Compartments:** Logical containers for resources
    - **Policies:** Rules that grant permissions
    - **Identity Domains:** Containers for users and groups
    
    **Authentication:**
    - Username/password
    - API signing keys
    - Auth tokens
    - Multi-factor authentication (MFA)
    
    **Authorization:**
    - Policy-based
    - Least privilege principle
    - Explicit deny overrides allow
    
    📚 **Reference:** [IAM Overview](https://docs.oracle.com/iaas/Content/Identity/getstarted/identity-domains.htm)
    """)
    
    st.markdown("### IAM Domains, Users, Groups, and Compartments")
    
    st.markdown("""
    **Identity Domains:**
    - Container for users and groups
    - Separate authentication realm
    - Can have multiple domains per tenancy
    - Default domain created automatically
    
    **Users:**
    - Represent individual people or applications
    - Belong to identity domain
    - Can be in multiple groups
    - Assigned credentials (password, API keys)
    
    **Groups:**
    - Collection of users
    - Simplify policy management
    - Users inherit group permissions
    - Can be in multiple groups
    
    **Compartments:**
    - Logical containers for resources
    - Hierarchical structure
    - Isolate and organize resources
    - Control access via policies
    - Root compartment = tenancy
    
    **Best Practices:**
    - Use groups, not individual users in policies
    - Create compartments by project/team/environment
    - Implement least privilege
    - Regular access reviews
    
    📚 **Reference:** [Managing IAM](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm)
    """)
    
    st.markdown("### IAM Policies")
    
    st.markdown("""
    **Policy Syntax:**
    ```
    Allow <subject> to <verb> <resource-type> in <location> where <conditions>
    ```
    
    **Components:**
    - **Subject:** group, dynamic-group, any-user
    - **Verb:** inspect, read, use, manage
    - **Resource-type:** all-resources, instances, buckets, etc.
    - **Location:** tenancy, compartment
    - **Conditions:** Optional constraints
    
    **Verb Hierarchy:**
    - **inspect:** List resources
    - **read:** Inspect + get details
    - **use:** Read + use resource
    - **manage:** Full control (all permissions)
    
    **Example Policies:**
    ```
    Allow group Developers to manage instances in compartment Development
    Allow group DBAs to manage databases in compartment Production
    Allow group NetworkAdmins to manage virtual-network-family in tenancy
    ```
    
    **Policy Attachment:**
    - Attached to compartments
    - Inherited by sub-compartments
    - Evaluated together
    
    📚 **Reference:** [IAM Policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)
    """)
    
    st.markdown("### Dynamic Groups")
    
    st.markdown("""
    **What are Dynamic Groups?**
    - Groups of OCI resources (not users)
    - Membership based on matching rules
    - Resources automatically added/removed
    - Used in policies for resource-to-resource access
    
    **Matching Rules:**
    - Based on resource attributes
    - Instance OCID, compartment, tags
    - Multiple rules with AND/OR logic
    
    **Example Rules:**
    ```
    instance.compartment.id = 'ocid1.compartment.oc1...'
    instance.id = 'ocid1.instance.oc1...'
    tag.namespace.key = 'value'
    ```
    
    **Use Cases:**
    - Instances accessing Object Storage
    - Functions calling other services
    - Autonomous Database accessing Object Storage
    
    **Example Policy:**
    ```
    Allow dynamic-group AppServers to read buckets in compartment AppData
    ```
    
    📚 **Reference:** [Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
    """)
    
    st.markdown("### Network Sources and Tag-Based Access Control")
    
    st.markdown("""
    **Network Sources:**
    - Restrict access based on IP address
    - Public IP addresses or CIDR blocks
    - VCN OCIDs
    - Used in policy conditions
    
    **Example:**
    ```
    Allow group RemoteAdmins to manage all-resources in tenancy 
      where request.networksource.name='CorporateNetwork'
    ```
    
    **Tag-Based Access Control:**
    - Control access based on resource tags
    - Defined tags (structured)
    - Free-form tags (unstructured)
    
    **Tag Namespaces:**
    - Organize tags
    - Define tag keys
    - Set tag defaults
    
    **Example Policy:**
    ```
    Allow group Developers to manage instances in compartment Dev 
      where target.resource.tag.Environment='Development'
    ```
    
    **Use Cases:**
    - Environment-based access (Dev, Test, Prod)
    - Cost center allocation
    - Project-based access
    - Compliance requirements
    
    📚 **Reference:** [Tagging](https://docs.oracle.com/iaas/Content/Tagging/home.htm)
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🎯 Exam Preparation Tips</h4>
    <ul>
        <li><strong>Hands-on Practice:</strong> Create resources in OCI Free Tier</li>
        <li><strong>Documentation:</strong> Review official Oracle docs for each topic</li>
        <li><strong>Scenarios:</strong> Understand when to use each service/feature</li>
        <li><strong>Best Practices:</strong> Know recommended configurations</li>
        <li><strong>Troubleshooting:</strong> Understand common issues and solutions</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "1. Business Strategy":
    st.title("📊 Pillar 1: Business Strategy")
    st.markdown("### *Defining Success for Cloud Adoption*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    Business strategy focuses on creating and communicating a **formalized plan** for cloud adoption. 
    The business plan should define goals and identify required workstreams for successful adoption.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>🎯 Core Focus</h3>
    Creating a formalized plan that:
    <ul>
        <li>Defines organizational goals</li>
        <li>Identifies required workstreams</li>
        <li>Spans from executive sponsorship to technical implementation</li>
        <li>Supports cloud transformation</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Three Key Capabilities")
    
    st.markdown("### 1️⃣ Define Your Goals")
    st.markdown("""
    - Establish clear, measurable objectives for cloud adoption
    - Align cloud initiatives with business outcomes
    - Understand the economics of cloud migration
    - Identify key performance indicators (KPIs)
    """)
    
    st.markdown("### 2️⃣ Build a Business Case")
    st.markdown("""
    - Support human, financial, and technological investments
    - Evaluate **Total Cost of Ownership (TCO)**
    - Prepare for shift from on-premises IT procurement to cloud-based investment model
    - Address vendor transition considerations
    - Justify resource allocation
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>💡 Important Concept: TCO Evaluation</h4>
    Total Cost of Ownership evaluation ensures organizations are prepared to:
    <ul>
        <li>Shift vendors if necessary</li>
        <li>Evolve from on-premises IT procurement process</li>
        <li>Adopt cloud-based investment model</li>
        <li>Account for hidden costs and long-term benefits</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Document the Business Value")
    st.markdown("""
    - Track and report on business value achieved
    - Measure success of first cloud adoption project
    - Prepare organization to prioritize next initiatives
    - Demonstrate ROI to stakeholders
    - Build momentum for continued cloud adoption
    """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tips</h3>
    <ul>
        <li><strong>Remember the three capabilities:</strong> Define Goals → Build Business Case → Document Value</li>
        <li><strong>TCO is critical:</strong> It's specifically mentioned as ensuring readiness for vendor shifts and procurement model evolution</li>
        <li><strong>Business strategy comes first:</strong> It's the foundation that connects business goals to technology solutions</li>
        <li><strong>Documentation matters:</strong> Reporting business value prepares for the next cloud initiative</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "2. People Strategy":
    st.title("👥 Pillar 2: People Strategy")
    st.markdown("### *Preparing the Human Elements for Success*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    People are the **most important aspect** of any project. The people strategy pillar helps organizations 
    define roles, responsibilities, and changes needed across the organization.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>🎯 Core Principle</h3>
    <strong>"The most important aspect to consider is people."</strong>
    <br><br>
    The people strategy pillar helps organizations:
    <ul>
        <li>Define roles and responsibilities</li>
        <li>Identify organizational changes needed</li>
        <li>Drive engagement</li>
        <li>Position teams for success</li>
        <li>Bring value back to the business</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Three Key Capabilities")
    
    st.markdown("### 1️⃣ Create a Cloud Center of Excellence (CCOE)")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>What is a CCOE?</h4>
    An <strong>extended multidisciplinary team</strong> that includes both business and technical stakeholders.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **CCOE Responsibilities:**
    - **Sponsor and guide** the cloud adoption initiative
    - **Lead** organizational change management process
    - **Define** roles and responsibilities for business and technical users
    - **Create** training plans
    - **Bridge** business and technical stakeholders
    """)
    
    st.markdown("### 2️⃣ Develop a Workforce Training and Readiness Plan")
    st.markdown("""
    - Assess current skill levels
    - Identify skill gaps
    - Create comprehensive training programs
    - Ensure teams are prepared for cloud technologies
    - Plan for ongoing learning and development
    - Address both technical and business user needs
    """)
    
    st.markdown("### 3️⃣ Create a Change Management Plan")
    st.markdown("""
    - Manage organizational transformation
    - Address resistance to change
    - Communicate benefits and expectations
    - Ensure smooth transition
    - Monitor and adjust as needed
    - Maintain stakeholder engagement
    """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tips</h3>
    <ul>
        <li><strong>CCOE is central:</strong> It's an extended multidisciplinary team with both business AND technical stakeholders</li>
        <li><strong>CCOE leads change management:</strong> Its role is to lead the organizational change management process</li>
        <li><strong>Three key capabilities:</strong> CCOE → Training/Readiness → Change Management</li>
        <li><strong>People come first:</strong> The framework explicitly states people are the most important aspect</li>
        <li><strong>Roles and responsibilities:</strong> CCOE defines these for both business and technical users</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "3. Security (Shared Model)":
    st.title("🔒 Pillar 3: Security - Shared Security Model")
    st.markdown("### *Understanding Shared Responsibility*")
    st.markdown("---")
    
    st.markdown("""
    ## Core Principle
    
    **Security in the cloud is a SHARED RESPONSIBILITY between you and Oracle.**
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>🎯 Key Understanding</h3>
    <ul>
        <li><strong>Oracle:</strong> Ensures security OF the cloud (infrastructure and operations)</li>
        <li><strong>Customer:</strong> Defines security IN the cloud (data, applications, configurations)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Shared Security Model Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🏢 Customer Responsibilities
        **Security IN the Cloud**
        
        #### Data & Access
        - Organization's data
        - User credentials and account information
        - Account access management
        - Application management
        - Secure user access behavior
        
        #### IAM & Policies
        - Strong OCI IAM policies
        - Identity and Access Management
        - VCN configuration
        
        #### Infrastructure Config
        - Patching (OS, applications)
        - Network and firewall configuration
        - Security rules and route rules
        - Virtual Cloud Network (VCN) setup
        
        #### Encryption & Storage
        - Client-side encryption
        - Vault management
        - Data security in databases and storage
        
        #### Overall Governance
        - Platforms created in OCI
        - Applications security and compliance
        - Overall governance, risk, and security of workloads
        """)
    
    with col2:
        st.markdown("""
        ### ☁️ Oracle Responsibilities
        **Security OF the Cloud**
        
        #### Infrastructure Services
        - OCI services and functionality:
          - Load Balancing
          - WAF (Web Application Firewall)
          - Cloud Guard
          - DDoS protection
        
        #### Isolation & Framework
        - Compute isolation
        - Network isolation
        - Storage isolation
        - IAM framework
        
        #### Physical Security
        - Data center physical security
        - Hardware security
        - Software infrastructure
        - Networking infrastructure
        - Facilities that run Oracle services
        
        #### Regional Infrastructure
        - Availability domains
        - Fault domains
        - All aspects of physical security in each region
        """)
    
    st.markdown("""
    <div class="highlight-box">
    <h3>⚖️ Shared Responsibilities</h3>
    <strong>Both Oracle and Customer are responsible for:</strong>
    <ul>
        <li>Security of software</li>
        <li>Associated logical configurations</li>
        <li>Security controls</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Security Best Practices in CAF")
    
    st.markdown("""
    The security pillar guides organizations to:
    
    1. **Define secure cloud architecture**
       - Establish foundational security aspects
       - Protect data and minimize risks
    
    2. **Implement right security controls**
       - Identify appropriate controls for your workloads
       - Apply defense-in-depth strategies
    
    3. **Monitor and prevent issues**
       - Watch for configuration drift
       - Implement continuous monitoring
       - Prevent security incidents
    """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tips</h3>
    <ul>
        <li><strong>Shared responsibility is key:</strong> Know what Oracle manages vs. what customers manage</li>
        <li><strong>Customer owns data:</strong> All customer data, credentials, and account information</li>
        <li><strong>Customer configures:</strong> Patching, network/firewall config, VCN, security rules, IAM policies</li>
        <li><strong>Oracle owns physical:</strong> Data centers, hardware, availability/fault domains</li>
        <li><strong>Oracle provides services:</strong> Load Balancing, WAF, Cloud Guard, DDoS protection, IAM framework</li>
        <li><strong>Both share:</strong> Software security and logical configurations</li>
        <li><strong>Three security goals:</strong> Define architecture → Implement controls → Monitor/prevent</li>
        <li><strong>Configuration drift:</strong> Specifically mentioned as something to monitor and prevent</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "4. Process Design":
    st.title("⚙️ Pillar 4: Process Design")
    st.markdown("### *Adapting Business and Technical Processes*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    Process design focuses on **adapting, implementing, and defining** the business and technical processes 
    (such as IT processes) needed to achieve business goals.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>⚠️ Why Process Design Matters</h3>
    <strong>Ineffective processes during cloud adoption can lead to:</strong>
    <ul>
        <li>Escalated costs due to resource mismanagement</li>
        <li>Compromised data security and compliance breaches</li>
        <li>Performance bottlenecks causing downtime</li>
        <li>Poor user experience</li>
        <li>Vendor lock-in limiting flexibility</li>
        <li>Potential data loss or service interruptions</li>
        <li>Misalignment with business goals</li>
        <li>Increased complexity and management challenges</li>
        <li>Employee resistance</li>
        <li>Insufficient scalability and adaptability</li>
        <li>Missed opportunities for innovation and cost savings</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Importance of Process")
    
    st.markdown("""
    Process design enables a **shared understanding** of:
    - Organization's needs
    - Challenges
    - Goals
    
    **Business and IT teams must work together** to:
    - Identify and prioritize business processes
    - Identify critical data and systems
    - Develop enterprise architecture aligned with strategic objectives
    - Achieve goals efficiently and effectively
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🤝 Collaboration is Key</h4>
    <ul>
        <li><strong>Business-IT collaboration:</strong> Crucial for defining enterprise architecture</li>
        <li><strong>Governance:</strong> Ensures alignment with organizational goals</li>
        <li><strong>Risk and compliance framework:</strong> Minimizes risk and maintains regulatory adherence</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Three Key Capabilities")
    
    st.markdown("### 1️⃣ Define Your Enterprise Architecture")
    st.markdown("""
    - Create comprehensive architecture blueprint
    - Align technology with business strategy
    - Identify critical systems and data flows
    - Plan for integration and interoperability
    - Consider hybrid and multi-cloud scenarios
    """)
    
    st.markdown("### 2️⃣ Establish a Governance Process")
    st.markdown("""
    - Define decision-making frameworks
    - Establish policies and standards
    - Ensure alignment with organizational goals
    - Create accountability structures
    - Monitor compliance with governance policies
    - Balance control with agility
    """)
    
    st.markdown("### 3️⃣ Meet Risk Management and Compliance Requirements")
    st.markdown("""
    - Identify and assess risks
    - Implement risk mitigation strategies
    - Ensure regulatory compliance
    - Maintain adherence to industry standards
    - Create audit trails
    - Establish compliance monitoring processes
    """)
    
    st.markdown("## Critical Success Factors")
    
    st.markdown("""
    To avoid adverse outcomes, ensure:
    - **Meticulous planning**
    - **Proper training**
    - **Effective communication**
    - **Ongoing management**
    - **Collaboration with knowledgeable cloud consultants or partners**
    """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tips</h3>
    <ul>
        <li><strong>Know the consequences:</strong> Understand what happens with ineffective processes (11 specific adverse outcomes listed)</li>
        <li><strong>Three capabilities:</strong> Enterprise Architecture → Governance → Risk/Compliance</li>
        <li><strong>Business-IT collaboration:</strong> Essential for defining enterprise architecture</li>
        <li><strong>Shared understanding:</strong> Process enables shared understanding of needs, challenges, and goals</li>
        <li><strong>Governance role:</strong> Ensures alignment with organizational goals</li>
        <li><strong>Risk framework:</strong> Minimizes risk AND maintains regulatory adherence</li>
        <li><strong>Multiple cloud scenarios:</strong> Process design helps evaluate multi-vendor cloud or hybrid environments</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "5. Technology Implementation":
    st.title("🛠️ Pillar 5: Technology Implementation")
    st.markdown("### *Transforming Plans into Cloud Reality*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    Technology implementation transforms business and technical processes into a **personalized, secure cloud environment** 
    that meets organizational needs.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>🎯 Core Concept: Landing Zones</h3>
    <strong>Landing Zone:</strong> A cloud environment built from an automated template that serves as the foundation 
    for cloud deployment.
    <br><br>
    <strong>Purpose:</strong>
    <ul>
        <li>Migrate existing on-premises data center solutions</li>
        <li>Create new cloud-native solutions</li>
        <li>Address business goals</li>
        <li>Provide secure, scalable foundation</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## OCI Landing Zone Options")
    
    st.markdown("### 1️⃣ OCI Core Landing Zone")
    st.markdown("""
    **Primary, standardized landing zone solution**
    
    **Features:**
    - Generic blueprint for secure, scalable, and resilient OCI tenancy
    - **CIS-compliant** (Center for Internet Security)
    - Supports complex architectures:
      - Multi-tenancy
      - Multi-cloud
    - Third-party integrations:
      - Firewall
      - SIEM (Security Information and Event Management)
    
    **Note:** Unifies the previous CIS Landing Zone and OCI Enterprise Landing Zone (OELZ)
    """)
    
    st.markdown("### 2️⃣ OCI Operating Entities Landing Zone")
    st.markdown("""
    **For organizations with functional divisions**
    
    **Features:**
    - Open assets and best practices
    - Simplifies onboarding for each Operating Entity (OE)
    - Includes blueprints with:
      - Designs
      - Declarative Infrastructure as Code (IaC)
    - Reduces design and implementation timelines
    - Reduces costs and efforts
    - Enables future-proof OCI with complete security and scalability
    """)
    
    st.markdown("### 3️⃣ OCI SCCA Landing Zone")
    st.markdown("""
    **Secure Cloud Computing Architecture for U.S. Department of Defense**
    
    **Options:**
    - Mission Owner landing zone
    - Managed SCCA Broker landing zone
    
    **Purpose:** Supports SCCA requirements for DoD
    """)
    
    st.markdown("### 4️⃣ OCI Zero Trust Landing Zone")
    st.markdown("""
    **Implements Zero Trust security model**
    
    **Based on standards from:**
    - NIST (National Institute of Standards and Technology)
    - CISA (Cybersecurity and Infrastructure Security Agency)
    - NCSC (UK National Cyber Security Centre)
    
    **Additional services beyond CIS Benchmarks:**
    - Zero-trust Packet Routing (ZPR)
    - Access Governance
    - Third-party ZTNA (Zero Trust Network Access) integration:
      - Fortinet
      - Palo Alto Networks
      - Others
    """)
    
    st.markdown("### 5️⃣ OCI Multicloud Landing Zones (OMCLZ)")
    st.markdown("""
    **Extends OCI to other cloud providers**
    
    **OMCLZ for Azure:**
    - AzureRM-based Terraform modules
    - AzAPI-based Azure Verified Modules (AVM)
    - Terraform templates for Oracle Exadata Database end-to-end:
      - Exadata infrastructure
      - VM cluster
      - DB Home
      - Container Database across Azure and OCI
    
    **OMCLZ for Google Cloud:**
    - Terraform modules, templates, examples, tutorials
    - Automates Oracle Database@Google Cloud deployment
    - Use cases:
      - Autonomous AI Database (ADB-S) provisioning
      - Client VM with SQL*Plus
      - ADB-S as vector database for RAG-based chatbots
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h3>🏗️ After Landing Zone Deployment</h3>
    <strong>Oracle Architecture Center provides:</strong>
    <ul>
        <li>Vetted design patterns</li>
        <li>Reference architectures</li>
        <li>Solution playbooks</li>
        <li>Deployment code</li>
        <li>Expert guidance from Oracle architects and developers</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Designing for Reliability")
    
    st.markdown("### Three Key Principles:")
    
    st.markdown("""
    **1. Extreme Reliability**
    - Design for maximum uptime
    - Minimize single points of failure
    - Implement redundancy at all levels
    
    **2. High Availability (HA)**
    - Ensure maximum potential for uptime and accessibility
    - Design systems to remain operational
    - Plan for component failures
    
    **3. Disaster Recovery (DR)**
    - Well-architected DR plan
    - Recover quickly from disasters
    - Continue providing services to users
    - Minimize data loss and downtime
    """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tips</h3>
    <ul>
        <li><strong>Landing Zone definition:</strong> Cloud environment built from automated template, serves as foundation</li>
        <li><strong>Five landing zone types:</strong> Core, Operating Entities, SCCA, Zero Trust, Multicloud</li>
        <li><strong>Core Landing Zone:</strong> Primary solution, CIS-compliant, unifies previous CIS LZ and OELZ</li>
        <li><strong>Operating Entities:</strong> Uses IaC, reduces timelines and costs</li>
        <li><strong>SCCA:</strong> For U.S. DoD, two options (Mission Owner or Managed SCCA Broker)</li>
        <li><strong>Zero Trust:</strong> Based on NIST/CISA/NCSC, includes ZPR and Access Governance</li>
        <li><strong>Multicloud:</strong> Extends to Azure and Google Cloud, uses Terraform</li>
        <li><strong>Three reliability principles:</strong> Extreme Reliability, HA, DR</li>
        <li><strong>Oracle Architecture Center:</strong> Provides design patterns, reference architectures, playbooks, deployment code</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "6. Management & Operations":
    st.title("📈 Pillar 6: Management and Operations")
    st.markdown("### *Keeping Your Cloud Running Smoothly*")
    st.markdown("---")
    
    st.markdown("""
    ## Overview
    
    Management and operations focuses on **what happens AFTER** your new cloud environment is up and running 
    in the landing zone.
    """)
    
    st.markdown("""
    <div class="key-concept">
    <h3>🎯 Core Purpose</h3>
    Help technology teams to:
    <ul>
        <li>Keep cloud environment running smoothly</li>
        <li>Optimize for performance</li>
        <li>Optimize for cost</li>
        <li>Position organization for growth as business demands require</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Three Key Capabilities")
    
    st.markdown("### 1️⃣ Observe and Manage Your Cloud Environment")
    
    st.markdown("""
    **Monitoring and Visibility:**
    - Implement comprehensive monitoring solutions
    - Track performance metrics
    - Monitor resource utilization
    - Set up alerts and notifications
    - Gain visibility into all cloud resources
    
    **Audit and Compliance:**
    - Maintain audit trails
    - Track changes and access
    - Ensure compliance with policies
    - Generate compliance reports
    - Monitor security posture
    
    **Management Activities:**
    - Day-to-day operations
    - Resource provisioning
    - Access management
    - Configuration management
    - Patch management
    """)
    
    st.markdown("### 2️⃣ Optimize Your Cloud Environment")
    
    st.markdown("""
    **Performance Optimization:**
    - Identify performance bottlenecks
    - Right-size resources
    - Optimize application performance
    - Improve response times
    - Enhance user experience
    
    **Cost Optimization:**
    - Analyze spending patterns
    - Identify cost-saving opportunities
    - Eliminate waste
    - Right-size instances
    - Use reserved capacity where appropriate
    - Implement cost allocation and chargeback
    
    **Resource Optimization:**
    - Optimize resource allocation
    - Automate scaling
    - Improve efficiency
    - Consolidate workloads where possible
    """)
    
    st.markdown("### 3️⃣ Design a Support and Incident Management Strategy")
    
    st.markdown("""
    **Support Strategy:**
    - Define support tiers and SLAs
    - Establish escalation procedures
    - Create support documentation
    - Train support teams
    - Implement self-service options
    
    **Incident Management:**
    - Establish incident response procedures
    - Define severity levels
    - Create runbooks for common issues
    - Implement incident tracking
    - Conduct post-incident reviews
    - Continuous improvement based on lessons learned
    
    **Business Continuity:**
    - Ensure rapid response to incidents
    - Minimize downtime
    - Maintain service availability
    - Protect business operations
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h3>🔄 Continuous Improvement Cycle</h3>
    Management and Operations is an ongoing process:
    <ol>
        <li><strong>Monitor:</strong> Observe environment performance and health</li>
        <li><strong>Analyze:</strong> Identify issues and opportunities</li>
        <li><strong>Optimize:</strong> Improve performance and reduce costs</li>
        <li><strong>Respond:</strong> Handle incidents effectively</li>
        <li><strong>Learn:</strong> Incorporate lessons into future operations</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Key Focus Areas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Operational Excellence
        - Smooth day-to-day operations
        - Automated processes
        - Efficient resource management
        - Proactive monitoring
        - Quick issue resolution
        """)
    
    with col2:
        st.markdown("""
        ### Growth Readiness
        - Scalability planning
        - Capacity management
        - Performance headroom
        - Flexibility for new demands
        - Support for innovation
        """)
    
    st.markdown("""
    <div class="exam-tip">
    <h3>📝 Exam Tips</h3>
    <ul>
        <li><strong>Post-deployment focus:</strong> This pillar is about what happens AFTER the landing zone is running</li>
        <li><strong>Three capabilities:</strong> Observe/Manage → Optimize → Support/Incident Management</li>
        <li><strong>Dual optimization:</strong> Both performance AND cost optimization are key</li>
        <li><strong>Growth positioning:</strong> Prepare organization to grow as business demands require</li>
        <li><strong>Monitoring includes:</strong> Visibility and audit (not just performance monitoring)</li>
        <li><strong>Incident management:</strong> Design a strategy, not just react to incidents</li>
        <li><strong>Continuous process:</strong> Ongoing management, not one-time setup</li>
        <li><strong>Technology teams:</strong> This pillar specifically helps technology teams keep things running</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_chapter == "Quick Reference":
    st.title("📋 Quick Reference Guide")
    st.markdown("### *Key Concepts at a Glance*")
    st.markdown("---")
    
    st.markdown("## The Six Pillars - Summary")
    
    pillars_data = {
        "Pillar": ["1. Business Strategy", "2. People Strategy", "3. Security", "4. Process Design", 
                   "5. Technology Implementation", "6. Management & Operations"],
        "Focus": [
            "Defining success",
            "Human elements",
            "Shared responsibility",
            "Business & IT processes",
            "Landing zones",
            "Post-deployment"
        ],
        "Key Capabilities": [
            "Goals, Business Case, Value",
            "CCOE, Training, Change Mgmt",
            "Architecture, Controls, Monitoring",
            "Enterprise Arch, Governance, Risk/Compliance",
            "Landing Zones, Architecture Center, HA/DR",
            "Observe/Manage, Optimize, Support/Incident"
        ]
    }
    
    st.markdown("""
    | Pillar | Focus | Key Capabilities |
    |--------|-------|------------------|
    | 1. Business Strategy | Defining success | Goals, Business Case, Value |
    | 2. People Strategy | Human elements | CCOE, Training, Change Mgmt |
    | 3. Security | Shared responsibility | Architecture, Controls, Monitoring |
    | 4. Process Design | Business & IT processes | Enterprise Arch, Governance, Risk/Compliance |
    | 5. Technology Implementation | Landing zones | Landing Zones, Architecture Center, HA/DR |
    | 6. Management & Operations | Post-deployment | Observe/Manage, Optimize, Support/Incident |
    """)
    
    st.markdown("---")
    
    st.markdown("## Critical Concepts to Remember")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Cloud Adoption Framework
        - **Purpose:** Structured approach to cloud adoption
        - **Scope:** People, processes, AND technology
        - **Approach:** Phased transformation
        - **Nature:** Multilayered, organization-wide
        - **Flexibility:** Adaptable, iterative
        
        ### Business Strategy
        - **TCO:** Total Cost of Ownership evaluation
        - **Investment shift:** On-premises → Cloud-based
        - **Documentation:** Report business value
        - **Sequence:** Goals → Business Case → Value
        
        ### People Strategy
        - **Most important:** People are #1 priority
        - **CCOE:** Multidisciplinary (business + technical)
        - **CCOE role:** Lead change management
        - **Training:** Comprehensive workforce readiness
        
        ### Security
        - **Model:** Shared responsibility
        - **Oracle:** Security OF the cloud
        - **Customer:** Security IN the cloud
        - **Customer owns:** Data, credentials, IAM policies, patching, VCN config
        - **Oracle owns:** Physical security, infrastructure, IAM framework
        - **Configuration drift:** Monitor and prevent
        """)
    
    with col2:
        st.markdown("""
        ### Process Design
        - **Collaboration:** Business-IT partnership essential
        - **Three areas:** Enterprise Arch, Governance, Risk/Compliance
        - **Governance:** Ensures alignment with goals
        - **Risk framework:** Minimizes risk, maintains compliance
        - **Consequences:** 11 adverse outcomes if ineffective
        
        ### Technology Implementation
        - **Landing Zone:** Automated template foundation
        - **Five types:** Core, Operating Entities, SCCA, Zero Trust, Multicloud
        - **Core LZ:** CIS-compliant, unifies CIS LZ + OELZ
        - **Zero Trust:** NIST/CISA/NCSC based, includes ZPR
        - **Multicloud:** Azure and Google Cloud support
        - **Reliability:** Extreme Reliability, HA, DR
        - **Architecture Center:** Design patterns, playbooks, code
        
        ### Management & Operations
        - **Timing:** AFTER landing zone is running
        - **Dual optimization:** Performance AND cost
        - **Growth:** Position for business demand growth
        - **Three capabilities:** Observe/Manage, Optimize, Support
        - **Continuous:** Ongoing process, not one-time
        """)
    
    st.markdown("---")
    
    st.markdown("## Key Acronyms")
    
    acronyms = {
        "Acronym": ["CAF", "CCOE", "TCO", "IAM", "VCN", "SIEM", "IaC", "CIS", "OELZ", 
                    "SCCA", "ZPR", "ZTNA", "NIST", "CISA", "NCSC", "HA", "DR", "OMCLZ", 
                    "AVM", "ADB-S", "RAG"],
        "Full Form": [
            "Cloud Adoption Framework",
            "Cloud Center of Excellence",
            "Total Cost of Ownership",
            "Identity and Access Management",
            "Virtual Cloud Network",
            "Security Information and Event Management",
            "Infrastructure as Code",
            "Center for Internet Security",
            "OCI Enterprise Landing Zone",
            "Secure Cloud Computing Architecture",
            "Zero-trust Packet Routing",
            "Zero Trust Network Access",
            "National Institute of Standards and Technology",
            "Cybersecurity and Infrastructure Security Agency",
            "National Cyber Security Centre (UK)",
            "High Availability",
            "Disaster Recovery",
            "OCI Multicloud Landing Zones",
            "Azure Verified Modules",
            "Autonomous AI Database",
            "Retrieval-Augmented Generation"
        ]
    }
    
    st.markdown("""
    | Acronym | Full Form |
    |---------|----------|
    | CAF | Cloud Adoption Framework |
    | CCOE | Cloud Center of Excellence |
    | TCO | Total Cost of Ownership |
    | IAM | Identity and Access Management |
    | VCN | Virtual Cloud Network |
    | SIEM | Security Information and Event Management |
    | IaC | Infrastructure as Code |
    | CIS | Center for Internet Security |
    | OELZ | OCI Enterprise Landing Zone |
    | SCCA | Secure Cloud Computing Architecture |
    | ZPR | Zero-trust Packet Routing |
    | ZTNA | Zero Trust Network Access |
    | NIST | National Institute of Standards and Technology |
    | CISA | Cybersecurity and Infrastructure Security Agency |
    | NCSC | National Cyber Security Centre (UK) |
    | HA | High Availability |
    | DR | Disaster Recovery |
    | OMCLZ | OCI Multicloud Landing Zones |
    | AVM | Azure Verified Modules |
    | ADB-S | Autonomous AI Database |
    | RAG | Retrieval-Augmented Generation |
    """)



# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Oracle Cloud Infrastructure Cloud Adoption Framework Study Guide</strong></p>
    <p>Based on official Oracle documentation | For OCI Certification Preparation</p>
    <p><em>Remember: Cloud adoption is a journey, not a destination. Master the framework, understand the principles, 
    and you'll be well-prepared for success.</em></p>
</div>
""", unsafe_allow_html=True)
