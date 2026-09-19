/* =====================================================
   ZELIVO SPICES
   MAIN JAVASCRIPT
===================================================== */

document.addEventListener("DOMContentLoaded", function () {


    /* ================================================
       NAVBAR SCROLL
    ================================================ */

    const navbar =
        document.querySelector(".zelivo-navbar");

    window.addEventListener("scroll", function () {

        if (window.scrollY > 50) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    });


    /* ================================================
       BACK TO TOP
    ================================================ */

    const backToTop =
        document.getElementById("backToTop");

    if (backToTop) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 400) {

                backToTop.classList.add("show");

            } else {

                backToTop.classList.remove("show");

            }

        });


        backToTop.addEventListener("click", function () {

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        });

    }


    /* ================================================
       PRODUCT FILTER
    ================================================ */

    const filterButtons =
        document.querySelectorAll(".filter-btn");

    const productItems =
        document.querySelectorAll(".product-item");


    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const filter =
                button.getAttribute("data-filter");


            filterButtons.forEach(function (btn) {

                btn.classList.remove("active");

            });


            button.classList.add("active");


            productItems.forEach(function (item) {

                const category =
                    item.getAttribute("data-category");


                if (
                    filter === "all" ||
                    filter === category
                ) {

                    item.style.display = "";

                } else {

                    item.style.display = "none";

                }

            });

        });

    });


    /* ================================================
       CLOSE MOBILE NAVBAR AFTER CLICK
    ================================================ */

    const navLinks =
        document.querySelectorAll(
            ".navbar-nav .nav-link"
        );

    const navbarCollapse =
        document.querySelector(".navbar-collapse");


    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            if (
                navbarCollapse &&
                navbarCollapse.classList.contains("show")
            ) {

                const bsCollapse =
                    bootstrap.Collapse.getInstance(
                        navbarCollapse
                    );

                if (bsCollapse) {

                    bsCollapse.hide();

                }

            }

        });

    });


    /* ================================================
       IMAGE LAZY LOADING
    ================================================ */

    document
        .querySelectorAll("img")
        .forEach(function (img) {

            if (!img.hasAttribute("loading")) {

                img.setAttribute(
                    "loading",
                    "lazy"
                );

            }

        });


    /* ================================================
       SIMPLE REVEAL ANIMATION
    ================================================ */

    const revealElements =
        document.querySelectorAll(
            ".feature-card, .product-card, .testimonial-card"
        );


    const revealObserver =
        new IntersectionObserver(
            function (entries) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.style.opacity = "1";

                        entry.target.style.transform =
                            "translateY(0)";

                        revealObserver.unobserve(
                            entry.target
                        );

                    }

                });

            },
            {
                threshold: 0.1
            }
        );


    revealElements.forEach(function (element) {

        element.style.opacity = "0";

        element.style.transform =
            "translateY(25px)";

        element.style.transition =
            "opacity .7s ease, transform .7s ease";

        revealObserver.observe(element);

    });


});