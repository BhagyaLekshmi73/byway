// Testimonial slider 

document.addEventListener("DOMContentLoaded", function () {
    const testimonialList = document.querySelector(".content ul");
    const prevButton = document.querySelector(".arrow .one");
    const nextButton = document.querySelector(".arrow .two");
    const testimonials = document.querySelectorAll(".content ul li");
    let currentIndex = 0;
    
    testimonialList.style.transition = "transform 0.5s ease-in-out";

    function getVisibleItems() {
        if (window.innerWidth <= 768) return 1;
        if (window.innerWidth <= 980) return 2;
        return 3;
    }

    function updateWidth() {
        testimonialList.style.transition = "none";
        
        const visibleItems = getVisibleItems();
        const containerWidth = testimonialList.parentElement.clientWidth;
        const itemWidth = containerWidth / visibleItems;
        
        testimonials.forEach(item => {
            item.style.width = `${itemWidth}px`;
            item.style.transition = "all 0.5s ease-in-out";
        });

        testimonialList.style.width = `${itemWidth * testimonials.length}px`;
        
        testimonialList.offsetHeight;
        
        testimonialList.style.transition = "transform 0.5s ease-in-out";
        
        updateSlider();
    }

    function updateSlider() {
        const visibleItems = getVisibleItems();
        const itemWidth = testimonials[0].getBoundingClientRect().width;
        const maxIndex = testimonials.length - visibleItems;
        
        if (currentIndex > maxIndex) {
            currentIndex = maxIndex;
        }
        
        const offset = -(currentIndex * itemWidth);
        
        testimonialList.style.transform = `translateX(${offset}px)`;
    }

    nextButton.addEventListener("click", () => {
        const visibleItems = getVisibleItems();
        const maxIndex = testimonials.length - visibleItems;
        
        if (currentIndex < maxIndex) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateSlider();
    });

    prevButton.addEventListener("click", () => {
        const visibleItems = getVisibleItems();
        const maxIndex = testimonials.length - visibleItems;
        
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = maxIndex;
        }
        updateSlider();
    });

    updateWidth();
    
    let resizeTimeout;
    window.addEventListener("resize", () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {

            testimonialList.style.transition = "none";
            updateWidth();

            setTimeout(() => {
                testimonialList.style.transition = "transform 0.5s ease-in-out";
            }, 50);
        }, 100);
    });
});





// Calculating price

document.addEventListener("DOMContentLoaded", function () {
    const originalPriceElement = document.querySelector(".line"); 
    const discountedPriceElement = document.querySelector(".discounted-price");
    const discountElement = document.querySelector(".clr"); 

    if (originalPriceElement && discountedPriceElement && discountElement) {
        let originalPrice = parseFloat(originalPriceElement.textContent.replace("$", "").trim()); 
        let discountPercent = parseFloat(discountElement.textContent.replace("% Off", "").trim()); 

        if (!isNaN(originalPrice) && !isNaN(discountPercent) && originalPrice > 0) {
            const discountedPrice = originalPrice - (originalPrice * (discountPercent / 100));
            discountedPriceElement.textContent = `$${discountedPrice.toFixed(2)}`;
        }
    }
});

