<!--VARIABLES {"noPageTitle": true}-->

<p><img src="<!--path pict-->sample_picture.jpg" class="floatRight" /></p>

[TOC]

<p style="clear: both;"></p>


# What's that

Attempt of creating responsive documentation design.


# Materials

- W3Schools: [HTML Responsive Web Design](https://www.w3schools.com/html/html_responsive.asp)
- W3Schools: [Responsive Web Design - The Viewport](https://www.w3schools.com/css/css_rwd_viewport.asp)
- MDN: [Viewport concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Viewport_concepts)
- Youtube: [Introduction To Responsive Web Design - HTML & CSS Tutorial](
    https://www.youtube.com/watch?v=srvUrASNj0s), length: 4:11:03, Sep 18, 2019


# Status and problems

The solution works much better that it did. But it needs more study of HTML flexible design 
implementation.

- The following setting:

    ````wrapped
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
    ````
    
    in files `doc_src/templates/multipage.html` and `doc/layout/styles.css`.

- The best practices in activating and deactivating of the sidebar. Now it's done using
    JavaScript but probably pure CSS would be better. Also see
    [here](https://codepen.io/markcaron/pen/wdVmpB).

- If possible improve look and feel on mobile devices.

- Look at the admonition problem:

    ![](<!--path pict-->admonition_problem.png)
    
- Drop down menu is not scrolled if exceeds the page height:

    ![](<!--path pict-->menu_dropdown_problem.png)
    
    Also see SO: [Have a fixed position div that needs to scroll if content overflows](
        https://stackoverflow.com/questions/16094785/have-a-fixed-position-div-that-needs-to-scroll-if-content-overflows).

- When content is scrolled horizontally, it's hidden behind the sidebar:

    ![](<!--path pict-->hidden_by_sidebar.png)



