document.addEventListener('DOMContentLoaded', () => {
    const services = {
        website: {
            title: 'Website Development',
            description: 'Crafting websites and software that adapt seamlessly to various devices, ensuring a consistent user experience.'
        },
        bespoke: {
            title: 'Bespoke Software',
            description: 'We create custom software tailored to your business needs. Our bespoke solutions are designed to optimize your workflows and increase efficiency.'
        },
        content: {
            title: 'Content Strategy',
            description: 'Crafting a comprehensive content strategy tailored to your business goals, ensuring your content engages and converts your target audience.'
        },
        ui: {
            title: 'UI Design',
            description: 'Creating intuitive and visually appealing user interfaces that enhance user experience and drive engagement.'
        },
        ecommerce: {
            title: 'E-commerce',
            description: 'Building robust e-commerce solutions that enable seamless online transactions and enhance your customers\' shopping experience.'
        },
        digitalMarketing: {
            title: 'Digital Marketing',
            description: 'Executing strategic digital marketing campaigns to boost your online presence, drive traffic, and increase conversions.'
        },
        maintenance: {
            title: 'Maintenance & Support',
            description: 'Providing ongoing maintenance and support services to ensure your software and websites run smoothly and securely.'
        },
        analytics: {
            title: 'Analytics & Performance',
            description: 'Leveraging data analytics to track and optimize the performance of your digital assets, driving continuous improvement.'
        }
    };

    const modalTitleElement = document.getElementById('serviceModalLabel');
    const modalDescriptionElement = document.getElementById('modalDescription');

    document.querySelectorAll('.thumbnail-classic-title a').forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const serviceKey = link.getAttribute('data-service');
            const service = services[serviceKey];
            modalTitleElement.textContent = service.title;
            modalDescriptionElement.textContent = service.description;
        });
    });
});
