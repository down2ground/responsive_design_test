<!--VARIABLES {"noPageTitle": true}-->

<p><img src="<!--path pict-->sample_picture.jpg" class="floatRight" /></p>

[TOC]

<p style="clear: both;"></p>


# What's that

Attempt of creating responsive documentation design.


# Materials

[[1](<!--page refs-->#ref_1), [2](<!--page refs-->#ref_2), [3](<!--page refs-->#ref_3), 
[4](<!--page refs-->#ref_4)]


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

- Existing styles

    ````
    a[name], a[id] {
        height: 42px;
        display: block;
        margin-top: -42px;
    }
    ````
    
    don't allow targeted links highlight:
    
    ````
    a[name]:target, a[id]:target, 
    h1[id]:target, h2[id]:target, h3[id]:target, 
    h4[id]:target, h5[id]:target, h6[id]:target {
        background-color: #fff9dc;
    }
    ````
    
    ![](<!--path pict-->targeted_links_problem.png)






