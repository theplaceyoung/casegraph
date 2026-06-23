fetch("../generated/graph.json")

.then(res=>res.json())

.then(data=>{

const cy = cytoscape({

container: document.getElementById("cy"),

elements:[
...data.nodes,
...data.edges
],

style:[

{
selector:"node",

style:{

'label':'data(label)',

'text-valign':'center',

'text-halign':'center'
}
},

{
selector:"edge",

style:{

'label':'data(label)',

'curve-style':'bezier',

'target-arrow-shape':'triangle'
}
}

],

layout:{

name:"cose"

}

})

})