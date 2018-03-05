import overpy
import overpass
import json


def PrintWayts(result):
    for way in result.ways:
        print("Name: {0}, Id = {1}".format(way.tags.get("name", "n/a"), way.id))
       # print("  Highway: %s" % way.tags.get("highway", "n/a"))
        print("  Tags:")
        for tag in way.tags:
            print("    Tag:   %s : %s" % (tag , way.tags[tag]) )
        print("  Nodes:")
        for node in way.nodes:
            #print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
            print("%f,%f" % (node.lat, node.lon))

def PrintWaytsHighway(result):
    print("ways Highway set: ")
    empty = "n/a"
    highwaySet = set()
    for way in result.ways:
        highway = way.tags.get("highway",empty )
        if(highway != empty):
            highwaySet.add(highway)
    print(highwaySet)

def RunQuery(api):
    result = api.query("""[timeout:25]
    [out:json]
    ;
    (
      node
        ["highway"]
        ["highway"!="footway"]
        ["highway"!="pedestrian"]
        ["highway"!="steps"]
        ["-highway"!="path"]
    
        (53.3323,-6.2209,53.3700,-5.2937);
      way
        ["highway"]
        ["highway"!="footway"]
        ["highway"!="pedestrian"]
        ["highway"!="steps"]
        ["-highway"!="path"]
        (53.3323,-6.2209,53.3700,-5.2937);
      relation
        ["highway"]
        ["highway"!="footway"]
        ["highway"!="pedestrian"]
        ["highway"!="steps"]
        ["-highway"!="path"]
        (53.3323,-6.2209,53.3700,-5.2937);
    );
    out;
    >;
    out skel qt;""")
    return result


def NewRunQuery(api):
    result = api.query("""[timeout:25]
    [out:json]
    ;
    (
      way
        ["highway"=="motorway"]
        ["highway"=="motorway_link"]
        ["highway"=="steps"]
        (53.3323,-6.2209,53.3700,-5.2937);
    );
    out;
    >;
    out skel qt;""")
    return result


if __name__ == '__main__':
    api = overpy.Overpass()

    # a = overpass.API()
    # mapQuery = overpass.MapQuery(53.3323,-6.2209,53.3700,-5.293)
    # res = a.Get(mapQuery)

    result = RunQuery(api)
    print(len(result.nodes))
    print(len(result.ways))
    for node in result.nodes:
        print("%f,%f" % (node.lat, node.lon))
    PrintWayts(result)
    PrintWaytsHighway(result)

    with open('data.txt', 'w') as outfile:
        json.dump(result, outfile)





def test(api):
    result = api.query("""(relation["place"="city"](53.3323,-6.2209,53.3700,-5.2937););out meta;>;out meta qt;""")
    print(len(result.nodes))
    print(len(result.ways))
    # for node in result.nodes:
    #     #print(node.tags)
    #     print("%f,%f" % (node.lat, node.lon))
    for way in result.ways:
        for node in way.nodes:
            print("%f,%f" % (node.lat, node.lon))

# #result = api.query("node(53.1744,-6.5978,53.5545,-5.9312);out;")
# #result = api.query("node(53.3323,-6.2209,53.3700,-5.2937);out;")
#
# # fetch all ways and nodes
# result1 = api.query("""
#     way(53.3323,-6.2209,53.3700,-5.2937) ["highway=* and highway!=footway and highway!=pedestrian and -highway!=path"];
#     (._;>;);
#     out body;
#     """)
# result2 = api.query("""
#     node(53.3323,-6.2209,53.3700,-5.2937) ["highway=* and highway!=footway and highway!=pedestrian and -highway!=path"];
#     (._;>;);
#     out body;
#     """)
#
# result3 = api.query("""
#     relation(53.3323,-6.2209,53.3700,-5.2937) ["highway=* and highway!=footway and highway!=pedestrian and -highway!=path"];
#     (._;>;);
#     out body;
#     """)
#
# result = api.query("""<osm-script output="json" timeout="25">
#  ... <union>
#  ... <query type="node">
#  ... <has-kv k="highway"/>
#  ... <has-kv k="highway" modv="not" v="footway"/>
#  ... <has-kv k="highway" modv="not" v="pedestrian"/>
#  ... <has-kv k="highway" modv="not" v="steps"/>
#  ... <has-kv k="-highway" modv="not" v="path"/>
#  ... <bbox-query {{bbox}}/>
#  ... </query>
#  ... <query type="way">
#  ... <has-kv k="highway"/>
#  ... <has-kv k="highway" modv="not" v="footway"/>
#  ... <has-kv k="highway" modv="not" v="pedestrian"/>
# ... <has-kv k="highway" modv="not" v="steps"/>
# ... <has-kv k="-highway" modv="not" v="path"/>
# ... <bbox-query {{bbox}}/>
# ... </query>
# ... <query type="relation">
# ... <has-kv k="highway"/>
# ... <has-kv k="highway" modv="not" v="footway"/>
# ... <has-kv k="highway" modv="not" v="pedestrian"/>
# ... <has-kv k="highway" modv="not" v="steps"/>
# ... <has-kv k="-highway" modv="not" v="path"/>
# ... <bbox-query {{bbox}}/>
# ... </query>
# ... </union>
# ... </osm-script>""")
