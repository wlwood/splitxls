#!/usr/bin/env python
# encoding:utf-8


cate_strs = """
womens,dresses,Women/Dresses
womens,athletic-dresses,Women/Dresses
womens,maternity-dresses,Women/Dresses
womens,maternity-nursing-dresses,Women/Dresses
womens,medical-scrubs-dresses,Women/Dresses
womens,novelty-dresses,Women/Dresses
womens,fashion-t-shirts,Women/T-shirts
womens,medical-apparel-t-shirts,Women/T-shirts
womens,work-utility-t-shirts,Women/T-shirts
womens,polo-shirts,Women/T-shirts
womens,athletic-shirts,Women/T-shirts
womens,athletic-maternity-shirts,Women/T-shirts
womens,maternity-nursing-t-shirts,Women/T-shirts
womens,maternity-nursing-night-shirts,Women/T-shirts
womens,maternity-night-shirts,Women/T-shirts
womens,fashion-maternity-t-shirts,Women/T-shirts
womens,novelty-t-shirts,Women/T-shirts
womens,tank-top-and-cami-shirts,Women/T-shirts
womens,blouses,Women/Blouses
womens,button-down-shirts,Women/Blouses
womens,maternity-nursing-blouses,Women/Blouses
womens,maternity-nursing-button-down-shirts,Women/Blouses
womens,fashion-maternity-blouses,Women/Blouses
womens,fleece-outerwear-jackets,Women/Outerwear
womens,athletic-shell-jackets,Women/Outerwear
womens,bowling-jackets,Women/Outerwear
womens,rock-climbing-jackets,Women/Outerwear
womens,fleece-outerwear-jackets,Women/Outerwear
womens,athletic-shell-jackets,Women/Outerwear
womens,bowling-jackets,Women/Outerwear
womens,rock-climbing-jackets,Women/Outerwear
womens,cycling-jackets,Women/Outerwear
womens,football-jackets,Women/Outerwear
womens,golf-jackets,Women/Outerwear
womens,rugby-jackets,Women/Outerwear
womens,running-jackets,Women/Outerwear
womens,skiing-jackets,Women/Outerwear
womens,snowboarding-jackets,Women/Outerwear
womens,tennis-jackets,Women/Outerwear
womens,athletic-rain-jackets,Women/Outerwear
womens,rain-ponchos,Women/Outerwear
womens,windbreaker-jackets,Women/Outerwear
womens,outerwear-capes,Women/Outerwear
womens,fashion-transitional-jackets,Women/Outerwear
womens,denim-jackets,Women/Outerwear
womens,down-outerwear-coats,Women/Outerwear
womens,down-alternative-outerwear-coats,Women/Outerwear
womens,parkas,Women/Outerwear
womens,faux-fur-outerwear-coats,Women/Outerwear
womens,fur-outerwear-coats,Women/Outerwear
womens,faux-leather-outerwear-jackets,Women/Outerwear
womens,leather-outerwear-jackets,Women/Outerwear
womens,quilted-lightweight-jackets,Women/Outerwear
womens,anoraks,Women/Outerwear
womens,raincoats,Women/Outerwear
womens,trenchcoats,Women/Outerwear
womens,denim-outerwear-vests,Women/Outerwear
womens,down-outerwear-vests,Women/Outerwear
womens,fleece-outerwear-vests,Women/Outerwear
womens,fur-outerwear-vests,Women/Outerwear
womens,eather-outerwear-vests,Women/Outerwear
womens,pea-coats,Women/Outerwear
womens,wool-outerwear-coats,Women/Outerwear
womens,self-adhesive-bras,Women/Lingerie & Sleepwear
womens,bra-extenders,Women/Lingerie & Sleepwear
womens,breast-petals,Women/Lingerie & Sleepwear
womens,lingerie-bags,Women/Lingerie & Sleepwear
womens,lingerie-tape,Women/Lingerie & Sleepwear
womens,bra-inserts,Women/Lingerie & Sleepwear
womens,bra-straps,Women/Lingerie & Sleepwear
womens,bras,Women/Lingerie & Sleepwear
womens,minimizer-bras,Women/Lingerie & Sleepwear
womens,babydoll-lingerie,Women/Lingerie & Sleepwear
womens,chemises,Women/Lingerie & Sleepwear
womens,maternity-bras,Women/Lingerie & Sleepwear
womens,nursing-bras,Women/Lingerie & Sleepwear
womens,sports-bras,Women/Lingerie & Sleepwear
womens,bustiers,Women/Lingerie & Sleepwear
womens,corsets,Women/Lingerie & Sleepwear
womens,camisoles-lingerie,Women/Lingerie & Sleepwear
womens,garter-belts,Women/Lingerie & Sleepwear
womens,garters,Women/Lingerie & Sleepwear
womens,underwear,Women/Lingerie & Sleepwear
womens,g-string-underwear,Women/Lingerie & Sleepwear
womens,tanga-underwear,Women/Lingerie & Sleepwear
womens,thong-underwear,Women/Lingerie & Sleepwear
womens,hipster-panties,Women/Lingerie & Sleepwear
womens,body-shapers-undergarments,Women/Lingerie & Sleepwear
womens,shapewear-bodysuits,Women/Lingerie & Sleepwear
womens,shapewear-briefs,Women/Lingerie & Sleepwear
womens,pajama-tops,Women/Lingerie & Sleepwear
womens,pajama-sets,Women/Lingerie & Sleepwear
womens,bathrobes,Women/Lingerie & Sleepwear
womens,nightgowns,Women/Lingerie & Sleepwear
womens,pajama-bottoms,Women/Lingerie & Sleepwear
womens,pant-liner-slips,Women/Lingerie & Sleepwear
womens,apparel-half-slips,Women/Lingerie & Sleepwear
womens,apparel-full-slips,Women/Lingerie & Sleepwear
womens,waist-shapewear,Women/Lingerie & Sleepwear
womens,shapewear-tops,Women/Lingerie & Sleepwear
womens,thigh-shapewear,Women/Lingerie & Sleepwear
womens,shapewear-half-slips,Women/Lingerie & Sleepwear
womens,shapewear-full-slips,Women/Lingerie & Sleepwear
womens,cardigan-sweaters,Women/Knitwear
womens,pullover-sweaters,Women/Knitwear
womens,shrug-sweaters,Women/Knitwear
womens,sweater-vests,Women/Knitwear
womens,athletic-sweaters,Women/Knitwear
womens,maternity-cardigan-sweaters,Women/Knitwear
womens,maternity-pullover-sweaters,Women/Knitwear
womens,maternity-sweater-vests,Women/Knitwear
womens,fashion-swimsuit-bottoms-separates,Women/Swimwear
womens,fashion-bikini-sets,Women/Swimwear
womens,fashion-bikini-tops,Women/Swimwear
womens,fashion-board-shorts,Women/Swimwear
womens,fashion-swimwear-cover-ups,Women/Swimwear
womens,fashion-one-piece-swimsuits,Women/Swimwear
womens,athletic-swimming-apparel,Women/Swimwear
womens,athletic-technical-swimsuits,Women/Swimwear
womens,athletic-one-piece-swimsuits,Women/Swimwear
womens,athletic-two-piece-swimsuits,Women/Swimwear
womens,rash-guard-shirts,Women/Swimwear
womens,fashion-swimsuit-bottoms-separates,Women/Swimwear
womens,fashion-tankini-sets,Women/Swimwear
womens,fashion-tankini-tops,Women/Swimwear
womens,athletic-pants,Women/Pants
womens,athletic-sweatpants,Women/Pants
womens,athletic-track-pants,Women/Pants
womens,pants,Women/Pants
womens,business-suit-pants-sets,Women/Pants
womens,fashion-maternity-leggings-pants,Women/Leggings
womens,athletic-leggings,Women/Leggings
womens,leggings-pants,Women/Leggings
womens,maternity-jeans,Women/Jeans
womens,jeans,Women/Jeans
womens,skirts,Women/Skirts
womens,athletic-skirts,Women/Skirts
womens,athletic-maternity-skirts,Women/Skirts
womens,fashion-maternity-skirts,Women/Skirts
womens,jumpsuits-apparel,Women/Jumpsuit & Romper
womens,overalls,Women/Jumpsuit & Romper
womens,shorts,Women/Shorts
womens,athletic-maternity-shorts,Women/Shorts
womens,fashion-maternity-shorts,Women/Shorts
womens,athletic-shorts,Women/Shorts
womens,fashion-board-shorts,Women/Shorts
womens,briefs-underwear,Women/Plus Size
womens,base-layer-bottoms,Women/Plus Size
womens,base-layer-underwear,Women/Plus Size
womens,base-layer-sets,Women/Plus Size
womens,base-layer-tops,Women/Plus Size
womens,base-layer-underwear,Women/Plus Size
womens,tunic-shirts,Women/Plus Size
womens,boy-shorts-panties,Women/Plus Size
mens,athletic-pants,Men/Pants
mens,athletic-sweatpants,Men/Pants
mens,athletic-track-pants,Men/Pants
mens,casual-pants,Men/Pants
mens,jeans,Men/Denims & Jeans
mens,cargo-shorts,Mens/Shorts
mens,denim-shorts,Mens/Shorts
mens,flat-front-shorts,Mens/Shorts
mens,pleated-shorts,Mens/Shorts
mens,bikini-underwear,Men/Underwear
mens,boxer-briefs,Men/Underwear
mens,boxer-shorts,Men/Underwear
mens,briefs-underwear,Men/Underwear
mens,thong-underwear,Men/Underwear
mens,thermal-underwear-bottoms,Men/Underwear
mens,thermal-underwear-sets,Men/Underwear
mens,thermal-underwear-tops,Men/Underwear
mens,thermal-underwear-union-suits,Men/Underwear
mens,trunks-underwear,Men/Underwear
mens,undershirts,Men/Underwear
mens,down-outerwear-coats,Men/Outerwear
mens,down-alternative-outerwear-coats,Men/Outerwear
mens,fleece-outerwear-jackets,Men/Outerwear
mens,athletic-insulated-jackets,Men/Outerwear
mens,bowling-jackets,Men/Outerwear
mens,rock-climbing-jackets,Men/Outerwear
mens,cycling-jackets,Men/Outerwear
mens,football-jackets,Men/Outerwear
mens,golf-jackets,Men/Outerwear
mens,hunting-jackets,Men/Outerwear
mens,rugby-jackets,Men/Outerwear
mens,running-jackets,Men/Outerwear
mens,skiing-jackets,Men/Outerwear
mens,snowboarding-jackets,Men/Outerwear
mens,tennis-jackets,Men/Outerwear
mens,athletic-shell-jackets,Men/Outerwear
mens,down-outerwear-coats,Men/Outerwear
mens,down-alternative-outerwear-coats,Men/Outerwear
mens,fleece-outerwear-jackets,Men/Outerwear
mens,faux-leather-outerwear-jackets,Men/Outerwear
mens,leather-outerwear-jackets,Men/Outerwear
mens,cotton-lightweight-jackets,Men/Outerwear
mens,denim-jackets,Men/Outerwear
mens,golf-jackets,Men/Outerwear
mens,varsity-jackets,Men/Outerwear
mens,windbreaker-jackets,Men/Outerwear
mens,raincoats,Men/Outerwear
mens,trenchcoats,Men/Outerwear
mens,denim-outerwear-vests,Men/Outerwear
mens,down-outerwear-vests,Men/Outerwear
mens,fleece-outerwear-vests,Men/Outerwear
mens,fur-outerwear-vests,Men/Outerwear
mens,eather-outerwear-vests,Men/Outerwear
mens,wool-outerwear-coats,Men/Outerwear
mens,work-utility-outerwear,Men/Outerwear
mens,button-down-shirts,Men/Shirts
mens,dress-shirts,Men/Shirts
mens,henley-shirts,Men/Shirts
mens,polo-shirts,Men/Shirts
mens,fashion-t-shirts,Men/Tee & Tank Top
mens,medical-apparel-t-shirts,Men/Tee & Tank Top
mens,work-utility-t-shirts,Men/Tee & Tank Top
mens,tank-top-and-cami-shirts,Men/Tee & Tank Top
jewels,chain-necklaces,Jewelry/Necklaces
jewels,choker-necklaces,Jewelry/Necklaces
jewels,collar-necklaces,Jewelry/Necklaces
jewels,locket-necklaces,Jewelry/Necklaces
jewels,pearl-strands,Jewelry/Necklaces
jewels,pendant-enhancers,Jewelry/Necklaces
jewels,pendant-necklaces,Jewelry/Necklaces
jewels,pendants,Jewelry/Necklaces
jewels,strand-necklaces,Jewelry/Necklaces
jewels,torque-necklaces,Jewelry/Necklaces
jewels,y-shaped-necklaces,Jewelry/Necklaces
jewels,bracelets,Jewelry/Bracelets
jewels,bangle-bracelets,Jewelry/Bracelets
jewels,cuff-bracelets,Jewelry/Bracelets
jewels,identification-bracelets,Jewelry/Bracelets
jewels,link-bracelets,Jewelry/Bracelets
jewels,strand-bracelets,Jewelry/Bracelets
jewels,stretch-bracelets,Jewelry/Bracelets
jewels,tennis-bracelets,Jewelry/Bracelets
jewels,wrap-bracelets,Jewelry/Bracelets
jewels,charm-bracelets,Jewelry/Bracelets
jewels,italian-style-charm-starter-bracelets,Jewelry/Bracelets
jewels,link-charm-bracelets,Jewelry/Bracelets
jewels,snake-charm-bracelets,Jewelry/Bracelets
jewels,charms,Jewelry/Bracelets
jewels,bead-charms,Jewelry/Bracelets
jewels,clasp-style-charms,Jewelry/Bracelets
jewels,italian-style-single-charms,Jewelry/Bracelets
jewels,earrings,Jewelry/Earrings
jewels,clip-on-earrings,Jewelry/Earrings
jewels,ear-cuffs,Jewelry/Earrings
jewels,dangle-earrings,Jewelry/Earrings
jewels,hoop-earrings,Jewelry/Earrings
jewels,stud-earrings,Jewelry/Earrings
jewels,ball-earrings,Jewelry/Earrings
jewels,earring-jackets,Jewelry/Earrings
jewels,rings,Jewelry/Rings
jewels,band-style-rings,Jewelry/Rings
jewels,stackable-rings,Jewelry/Rings
jewels,statement-rings,Jewelry/Rings
jewels,engagement-rings,Jewelry/Rings
jewels,promise-rings,Jewelry/Rings
jewels,ring-enhancers,Jewelry/Rings
jewels,wedding-bands,Jewelry/Rings
jewels,anniversary-rings,Jewelry/Rings
jewels,diamond-bands,Jewelry/Rings
jewels,eternity-rings,Jewelry/Rings
jewels,plain-wedding-bands,Jewelry/Rings
jewels,jewelry-sets,Jewelry/Jewelry Sets
jewels,wedding-ring-sets,Jewelry/Jewelry Sets
jewels,body-Jewelry ,Jewelry/Piercing Jewelry
"""



cate_dict = {'womens': {'raincoats': 'Women/Outerwear', 'athletic-technical-swimsuits': 'Women/Swimwear', 'faux-fur-outerwear-coats': 'Women/Outerwear', 'athletic-maternity-shorts': 'Women/Shorts', 'polo-shirts': 'Women/T-shirts', 'sweater-vests': 'Women/Knitwear', 'garters': 'Women/Lingerie & Sleepwear', 'athletic-rain-jackets': 'Women/Outerwear', 'minimizer-bras': 'Women/Lingerie & Sleepwear', 'pajama-sets': 'Women/Lingerie & Sleepwear', 'athletic-one-piece-swimsuits': 'Women/Swimwear', 'lingerie-tape': 'Women/Lingerie & Sleepwear', 'lingerie-bags': 'Women/Lingerie & Sleepwear', 'athletic-shell-jackets': 'Women/Outerwear', 'fashion-one-piece-swimsuits': 'Women/Swimwear', 'sports-bras': 'Women/Lingerie & Sleepwear', 'pant-liner-slips': 'Women/Lingerie & Sleepwear', 'rain-ponchos': 'Women/Outerwear', 'quilted-lightweight-jackets': 'Women/Outerwear', 'athletic-pants': 'Women/Pants', 'shapewear-bodysuits': 'Women/Lingerie & Sleepwear', 'jumpsuits-apparel': 'Women/Jumpsuit & Romper', 'athletic-leggings': 'Women/Leggings', 'wool-outerwear-coats': 'Women/Outerwear', 'athletic-sweaters': 'Women/Knitwear', 'corsets': 'Women/Lingerie & Sleepwear', 'fashion-tankini-tops': 'Women/Swimwear', 'bra-inserts': 'Women/Lingerie & Sleepwear', 'maternity-jeans': 'Women/Jeans', 'breast-petals': 'Women/Lingerie & Sleepwear', 'skiing-jackets': 'Women/Outerwear', 'maternity-nursing-night-shirts': 'Women/T-shirts', 'maternity-nursing-button-down-shirts': 'Women/Blouses', 'self-adhesive-bras': 'Women/Lingerie & Sleepwear', 'down-outerwear-coats': 'Women/Outerwear', 'nursing-bras': 'Women/Lingerie & Sleepwear', 'shapewear-tops': 'Women/Lingerie & Sleepwear', 'fashion-bikini-sets': 'Women/Swimwear', 'rash-guard-shirts': 'Women/Swimwear', 'hipster-panties': 'Women/Lingerie & Sleepwear', 'chemises': 'Women/Lingerie & Sleepwear', 'business-suit-pants-sets': 'Women/Pants', 'medical-apparel-t-shirts': 'Women/T-shirts', 'medical-scrubs-dresses': 'Women/Dresses', 'boy-shorts-panties': 'Women/Plus Size', 'outerwear-capes': 'Women/Outerwear', 'fashion-swimsuit-bottoms-separates': 'Women/Swimwear', 'leggings-pants': 'Women/Leggings', 'novelty-dresses': 'Women/Dresses', 'thong-underwear': 'Women/Lingerie & Sleepwear', 'running-jackets': 'Women/Outerwear', 'garter-belts': 'Women/Lingerie & Sleepwear', 'tanga-underwear': 'Women/Lingerie & Sleepwear', 'pants': 'Women/Pants', 'maternity-nursing-blouses': 'Women/Blouses', 'athletic-maternity-shirts': 'Women/T-shirts', 'snowboarding-jackets': 'Women/Outerwear', 'bowling-jackets': 'Women/Outerwear', 'anoraks': 'Women/Outerwear', 'bra-straps': 'Women/Lingerie & Sleepwear', 'babydoll-lingerie': 'Women/Lingerie & Sleepwear', 'maternity-nursing-dresses': 'Women/Dresses', 'maternity-cardigan-sweaters': 'Women/Knitwear', 'bras': 'Women/Lingerie & Sleepwear', 'underwear': 'Women/Lingerie & Sleepwear', 'bra-extenders': 'Women/Lingerie & Sleepwear', 'pajama-bottoms': 'Women/Lingerie & Sleepwear', 'fur-outerwear-coats': 'Women/Outerwear', 'fashion-maternity-leggings-pants': 'Women/Leggings', 'athletic-track-pants': 'Women/Pants', 'skirts': 'Women/Skirts', 'fashion-maternity-skirts': 'Women/Skirts', 'pea-coats': 'Women/Outerwear', 'tank-top-and-cami-shirts': 'Women/T-shirts', 'maternity-pullover-sweaters': 'Women/Knitwear', 'blouses': 'Women/Blouses', 'denim-outerwear-vests': 'Women/Outerwear', 'jeans': 'Women/Jeans', 'maternity-sweater-vests': 'Women/Knitwear', 'down-outerwear-vests': 'Women/Outerwear', 'fashion-swimwear-cover-ups': 'Women/Swimwear', 'parkas': 'Women/Outerwear', 'tennis-jackets': 'Women/Outerwear', 'work-utility-t-shirts': 'Women/T-shirts', 'athletic-shirts': 'Women/T-shirts', 'golf-jackets': 'Women/Outerwear', 'button-down-shirts': 'Women/Blouses', 'base-layer-sets': 'Women/Plus Size', 'g-string-underwear': 'Women/Lingerie & Sleepwear', 'waist-shapewear': 'Women/Lingerie & Sleepwear', 'shorts': 'Women/Shorts', 'windbreaker-jackets': 'Women/Outerwear', 'base-layer-underwear': 'Women/Plus Size', 'thigh-shapewear': 'Women/Lingerie & Sleepwear', 'fashion-maternity-t-shirts': 'Women/T-shirts', 'apparel-half-slips': 'Women/Lingerie & Sleepwear', 'athletic-skirts': 'Women/Skirts', 'briefs-underwear': 'Women/Plus Size', 'body-shapers-undergarments': 'Women/Lingerie & Sleepwear', 'trenchcoats': 'Women/Outerwear', 'fleece-outerwear-vests': 'Women/Outerwear', 'fleece-outerwear-jackets': 'Women/Outerwear', 'base-layer-tops': 'Women/Plus Size', 'camisoles-lingerie': 'Women/Lingerie & Sleepwear', 'football-jackets': 'Women/Outerwear', 'athletic-dresses': 'Women/Dresses', 'rock-climbing-jackets': 'Women/Outerwear', 'fashion-board-shorts': 'Women/Shorts', 'fashion-tankini-sets': 'Women/Swimwear', 'nightgowns': 'Women/Lingerie & Sleepwear', 'bustiers': 'Women/Lingerie & Sleepwear', 'athletic-two-piece-swimsuits': 'Women/Swimwear', 'fashion-maternity-shorts': 'Women/Shorts', 'shapewear-half-slips': 'Women/Lingerie & Sleepwear', 'fashion-maternity-blouses': 'Women/Blouses', 'athletic-shorts': 'Women/Shorts', 'maternity-dresses': 'Women/Dresses', 'shrug-sweaters': 'Women/Knitwear', 'fur-outerwear-vests': 'Women/Outerwear', 'fashion-t-shirts': 'Women/T-shirts', 'eather-outerwear-vests': 'Women/Outerwear', 'maternity-nursing-t-shirts': 'Women/T-shirts', 'bathrobes': 'Women/Lingerie & Sleepwear', 'shapewear-full-slips': 'Women/Lingerie & Sleepwear', 'athletic-swimming-apparel': 'Women/Swimwear', 'maternity-night-shirts': 'Women/T-shirts', 'dresses': 'Women/Dresses', 'cycling-jackets': 'Women/Outerwear', 'pajama-tops': 'Women/Lingerie & Sleepwear', 'cardigan-sweaters': 'Women/Knitwear', 'fashion-bikini-tops': 'Women/Swimwear', 'down-alternative-outerwear-coats': 'Women/Outerwear', 'maternity-bras': 'Women/Lingerie & Sleepwear', 'leather-outerwear-jackets': 'Women/Outerwear', 'overalls': 'Women/Jumpsuit & Romper', 'apparel-full-slips': 'Women/Lingerie & Sleepwear', 'denim-jackets': 'Women/Outerwear', 'pullover-sweaters': 'Women/Knitwear', 'athletic-sweatpants': 'Women/Pants', 'shapewear-briefs': 'Women/Lingerie & Sleepwear', 'novelty-t-shirts': 'Women/T-shirts', 'tunic-shirts': 'Women/Plus Size', 'base-layer-bottoms': 'Women/Plus Size', 'rugby-jackets': 'Women/Outerwear', 'fashion-transitional-jackets': 'Women/Outerwear', 'athletic-maternity-skirts': 'Women/Skirts', 'faux-leather-outerwear-jackets': 'Women/Outerwear'}, 'jewels': {'anniversary-rings': 'Jewelry/Rings', 'link-bracelets': 'Jewelry/Bracelets', 'locket-necklaces': 'Jewelry/Necklaces', 'diamond-bands': 'Jewelry/Rings', 'clasp-style-charms': 'Jewelry/Bracelets', 'italian-style-charm-starter-bracelets': 'Jewelry/Bracelets', 'charm-bracelets': 'Jewelry/Bracelets', 'pendant-enhancers': 'Jewelry/Necklaces', 'bead-charms': 'Jewelry/Bracelets', 'tennis-bracelets': 'Jewelry/Bracelets', 'jewelry-sets': 'Jewelry/Jewelry Sets', 'identification-bracelets': 'Jewelry/Bracelets', 'ring-enhancers': 'Jewelry/Rings', 'earring-jackets': 'Jewelry/Earrings', 'pearl-strands': 'Jewelry/Necklaces', 'eternity-rings': 'Jewelry/Rings', 'hoop-earrings': 'Jewelry/Earrings', 'rings': 'Jewelry/Rings', 'stretch-bracelets': 'Jewelry/Bracelets', 'bangle-bracelets': 'Jewelry/Bracelets', 'stackable-rings': 'Jewelry/Rings', 'wedding-bands': 'Jewelry/Rings', 'plain-wedding-bands': 'Jewelry/Rings', 'earrings': 'Jewelry/Earrings', 'snake-charm-bracelets': 'Jewelry/Bracelets', 'torque-necklaces': 'Jewelry/Necklaces', 'dangle-earrings': 'Jewelry/Earrings', 'band-style-rings': 'Jewelry/Rings', 'ball-earrings': 'Jewelry/Earrings', 'charms': 'Jewelry/Bracelets', 'collar-necklaces': 'Jewelry/Necklaces', 'promise-rings': 'Jewelry/Rings', 'pendants': 'Jewelry/Necklaces', 'strand-bracelets': 'Jewelry/Bracelets', 'clip-on-earrings': 'Jewelry/Earrings', 'bracelets': 'Jewelry/Bracelets', 'strand-necklaces': 'Jewelry/Necklaces', 'italian-style-single-charms': 'Jewelry/Bracelets', 'link-charm-bracelets': 'Jewelry/Bracelets', 'y-shaped-necklaces': 'Jewelry/Necklaces', 'engagement-rings': 'Jewelry/Rings', 'wedding-ring-sets': 'Jewelry/Jewelry Sets', 'pendant-necklaces': 'Jewelry/Necklaces', 'stud-earrings': 'Jewelry/Earrings', 'ear-cuffs': 'Jewelry/Earrings', 'wrap-bracelets': 'Jewelry/Bracelets', 'cuff-bracelets': 'Jewelry/Bracelets', 'statement-rings': 'Jewelry/Rings', 'choker-necklaces': 'Jewelry/Necklaces'}, 'mens': {'henley-shirts': 'Men/Shirts', 'rock-climbing-jackets': 'Men/Outerwear', 'fleece-outerwear-vests': 'Men/Outerwear', 'denim-outerwear-vests': 'Men/Outerwear', 'medical-apparel-t-shirts': 'Men/Tee & Tank Top', 'undershirts': 'Men/Underwear', 'raincoats': 'Men/Outerwear', 'jeans': 'Men/Denims & Jeans', 'denim-shorts': 'Mens/Shorts', 'work-utility-outerwear': 'Men/Outerwear', 'polo-shirts': 'Men/Shirts', 'cotton-lightweight-jackets': 'Men/Outerwear', 'bikini-underwear': 'Men/Underwear', 'varsity-jackets': 'Men/Outerwear', 'thong-underwear': 'Men/Underwear', 'boxer-shorts': 'Men/Underwear', 'pleated-shorts': 'Mens/Shorts', 'golf-jackets': 'Men/Outerwear', 'running-jackets': 'Men/Outerwear', 'fur-outerwear-vests': 'Men/Outerwear', 'windbreaker-jackets': 'Men/Outerwear', 'athletic-insulated-jackets': 'Men/Outerwear', 'hunting-jackets': 'Men/Outerwear', 'athletic-shell-jackets': 'Men/Outerwear', 'boxer-briefs': 'Men/Underwear', 'cargo-shorts': 'Mens/Shorts', 'dress-shirts': 'Men/Shirts', 'cycling-jackets': 'Men/Outerwear', 'thermal-underwear-bottoms': 'Men/Underwear', 'work-utility-t-shirts': 'Men/Tee & Tank Top', 'tennis-jackets': 'Men/Outerwear', 'thermal-underwear-tops': 'Men/Underwear', 'down-alternative-outerwear-coats': 'Men/Outerwear', 'thermal-underwear-union-suits': 'Men/Underwear', 'flat-front-shorts': 'Mens/Shorts', 'fashion-t-shirts': 'Men/Tee & Tank Top', 'wool-outerwear-coats': 'Men/Outerwear', 'casual-pants': 'Men/Pants', 'athletic-track-pants': 'Men/Pants', 'bowling-jackets': 'Men/Outerwear', 'leather-outerwear-jackets': 'Men/Outerwear', 'down-outerwear-vests': 'Men/Outerwear', 'denim-jackets': 'Men/Outerwear', 'briefs-underwear': 'Men/Underwear', 'trunks-underwear': 'Men/Underwear', 'skiing-jackets': 'Men/Outerwear', 'athletic-sweatpants': 'Men/Pants', 'faux-leather-outerwear-jackets': 'Men/Outerwear', 'down-outerwear-coats': 'Men/Outerwear', 'fleece-outerwear-jackets': 'Men/Outerwear', 'eather-outerwear-vests': 'Men/Outerwear', 'snowboarding-jackets': 'Men/Outerwear', 'rugby-jackets': 'Men/Outerwear', 'trenchcoats': 'Men/Outerwear', 'tank-top-and-cami-shirts': 'Men/Tee & Tank Top', 'button-down-shirts': 'Men/Shirts', 'football-jackets': 'Men/Outerwear', 'thermal-underwear-sets': 'Men/Underwear'}}



def create_dict():
    """ 生成字典,最后再把字典贴到cate_dict """
    cate_dict = {}
    tmp_dict  = {}
    cate_strs_list = cate_strs.strip().split("\n")
    print len(cate_strs_list)
    for line in cate_strs_list:
        line_list = line.split(",")
        if len(line_list) < 3: continue
        key1 = line_list[0]
        key2 = line_list[1]
        value = line_list[2]
        if not key1: continue
        current_n = cate_strs_list.index(line)
        if line == cate_strs_list[-1]:
            lastline = True
        else:
            lastline = False
        if lastline:
            cate_dict[cate_strs_list[current_n].split(",")[0].lower()] = tmp_dict
            break
        if key1 not in cate_dict:
            if current_n == 0:
                tmp_dict[key2] = value
                cate_dict[key1.lower()] = {}
                continue
            else:
                cate_dict[cate_strs_list[current_n-1].split(",")[0].lower()] = tmp_dict
                cate_dict[key1.lower()]={}
                tmp_dict = {}
        else:
            if key2 in tmp_dict:
                print "重复的:", key1,",", key2,",", value
            tmp_dict[key2] = value
    return cate_dict



        
def find_cate(cate_type,cate_name):

    cate_value = ""
    try:
        cate_value = cate_dict.get(cate_type,{}).get(cate_name,"")
    except Exception,e:
        print "not found cate "
    return cate_value


        
if __name__ == "__main__":
    #print cate_dict.get("mens")
    c_dict  = create_dict()
    print c_dict
    #print c_dict.keys()
    #print c_dict.get("womens")
    #print c_dict.get("womens").get("pajama-tops")
    #print c_dict.keys()
    #print c_dict.get("jewels")
    print len(c_dict.get("womens")), len(c_dict.get("mens")), len(c_dict.get("jewels"))
    #print c_dict.get("womens").keys(), "dresses" in c_dict.get("womens").keys()
