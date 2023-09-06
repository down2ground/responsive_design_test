<!--VARIABLES {"noPageTitle": true}-->

<p><img src="<!--path pict-->sample_picture.jpg" class="floatRight" /></p>

[TOC]

<p style="clear: both;"></p>

----------------------------------------------------------------------------------------------------
# What's that

Attempt of creating responsive documentation design.

----------------------------------------------------------------------------------------------------
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
    JavaScript but probably pure CSS would be better. Also see [[6](<!--page refs-->#ref_6)].

- If possible improve look and feel on mobile devices.

- Look at the admonition problem:

    ![](<!--path pict-->admonition_problem.png)

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
    
    Also see SO: [CSS- Highlight a div when the id is linked to using an anchor?](
    https://stackoverflow.com/questions/11142125/css-highlight-a-div-when-the-id-is-linked-to-using-an-anchor).


----------------------------------------------------------------------------------------------------
# Resolved
    
- Drop down menu is not scrolled if exceeds the page height:

    ![](<!--path pict-->menu_dropdown_problem.png)
    
    Also see [[5](<!--page refs-->#ref_5)].

- Would be good to place the sidebar links like "Source text" and "GitHub" in one line:

    ![](<!--path pict-->place_in_one_line.png)


