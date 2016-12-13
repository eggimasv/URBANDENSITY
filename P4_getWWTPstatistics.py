
# This file reads out all WWTP file results

a = ['/mnt/project/eggimasv/P4/P4_CH_NEU/103100', '/mnt/project/eggimasv/P4/P4_CH_NEU/103500', '/mnt/project/eggimasv/P4/P4_CH_NEU/110200', '/mnt/project/eggimasv/P4/P4_CH_NEU/120200', '/mnt/project/eggimasv/P4/P4_CH_NEU/132200', '/mnt/project/eggimasv/P4/P4_CH_NEU/134800', '/mnt/project/eggimasv/P4/P4_CH_NEU/136700', '/mnt/project/eggimasv/P4/P4_CH_NEU/140100', '/mnt/project/eggimasv/P4/P4_CH_NEU/14101', '/mnt/project/eggimasv/P4/P4_CH_NEU/14201', '/mnt/project/eggimasv/P4/P4_CH_NEU/150200', '/mnt/project/eggimasv/P4/P4_CH_NEU/150700', '/mnt/project/eggimasv/P4/P4_CH_NEU/17201', '/mnt/project/eggimasv/P4/P4_CH_NEU/18001', '/mnt/project/eggimasv/P4/P4_CH_NEU/201700', '/mnt/project/eggimasv/P4/P4_CH_NEU/210100', '/mnt/project/eggimasv/P4/P4_CH_NEU/216100', '/mnt/project/eggimasv/P4/P4_CH_NEU/219600', '/mnt/project/eggimasv/P4/P4_CH_NEU/226500', '/mnt/project/eggimasv/P4/P4_CH_NEU/22701', '/mnt/project/eggimasv/P4/P4_CH_NEU/227200', '/mnt/project/eggimasv/P4/P4_CH_NEU/231000', '/mnt/project/eggimasv/P4/P4_CH_NEU/240700', '/mnt/project/eggimasv/P4/P4_CH_NEU/247200', '/mnt/project/eggimasv/P4/P4_CH_NEU/254501', '/mnt/project/eggimasv/P4/P4_CH_NEU/254600', '/mnt/project/eggimasv/P4/P4_CH_NEU/255400', '/mnt/project/eggimasv/P4/P4_CH_NEU/255600', '/mnt/project/eggimasv/P4/P4_CH_NEU/257500', '/mnt/project/eggimasv/P4/P4_CH_NEU/261900', '/mnt/project/eggimasv/P4/P4_CH_NEU/285100', '/mnt/project/eggimasv/P4/P4_CH_NEU/285300', '/mnt/project/eggimasv/P4/P4_CH_NEU/286600', '/mnt/project/eggimasv/P4/P4_CH_NEU/289400', '/mnt/project/eggimasv/P4/P4_CH_NEU/295200', '/mnt/project/eggimasv/P4/P4_CH_NEU/296300', '/mnt/project/eggimasv/P4/P4_CH_NEU/3001', '/mnt/project/eggimasv/P4/P4_CH_NEU/300202', '/mnt/project/eggimasv/P4/P4_CH_NEU/300600', '/mnt/project/eggimasv/P4/P4_CH_NEU/302100', '/mnt/project/eggimasv/P4/P4_CH_NEU/302401', '/mnt/project/eggimasv/P4/P4_CH_NEU/30400', '/mnt/project/eggimasv/P4/P4_CH_NEU/30600', '/mnt/project/eggimasv/P4/P4_CH_NEU/310200', '/mnt/project/eggimasv/P4/P4_CH_NEU/321700', '/mnt/project/eggimasv/P4/P4_CH_NEU/325600', '/mnt/project/eggimasv/P4/P4_CH_NEU/327200', '/mnt/project/eggimasv/P4/P4_CH_NEU/327400', '/mnt/project/eggimasv/P4/P4_CH_NEU/327600', '/mnt/project/eggimasv/P4/P4_CH_NEU/329501', '/mnt/project/eggimasv/P4/P4_CH_NEU/333201', '/mnt/project/eggimasv/P4/P4_CH_NEU/333500', '/mnt/project/eggimasv/P4/P4_CH_NEU/333800', '/mnt/project/eggimasv/P4/P4_CH_NEU/340802', '/mnt/project/eggimasv/P4/P4_CH_NEU/3501', '/mnt/project/eggimasv/P4/P4_CH_NEU/350501', '/mnt/project/eggimasv/P4/P4_CH_NEU/35100', '/mnt/project/eggimasv/P4/P4_CH_NEU/351101', '/mnt/project/eggimasv/P4/P4_CH_NEU/352101', '/mnt/project/eggimasv/P4/P4_CH_NEU/356101', '/mnt/project/eggimasv/P4/P4_CH_NEU/359901', '/mnt/project/eggimasv/P4/P4_CH_NEU/360301', '/mnt/project/eggimasv/P4/P4_CH_NEU/366101', '/mnt/project/eggimasv/P4/P4_CH_NEU/371201', '/mnt/project/eggimasv/P4/P4_CH_NEU/373201', '/mnt/project/eggimasv/P4/P4_CH_NEU/373402', '/mnt/project/eggimasv/P4/P4_CH_NEU/374201', '/mnt/project/eggimasv/P4/P4_CH_NEU/376101', '/mnt/project/eggimasv/P4/P4_CH_NEU/378601', '/mnt/project/eggimasv/P4/P4_CH_NEU/382101', '/mnt/project/eggimasv/P4/P4_CH_NEU/385104', '/mnt/project/eggimasv/P4/P4_CH_NEU/400100', '/mnt/project/eggimasv/P4/P4_CH_NEU/402700', '/mnt/project/eggimasv/P4/P4_CH_NEU/407900', '/mnt/project/eggimasv/P4/P4_CH_NEU/408200', '/mnt/project/eggimasv/P4/P4_CH_NEU/412200', '/mnt/project/eggimasv/P4/P4_CH_NEU/416700', '/mnt/project/eggimasv/P4/P4_CH_NEU/422900', '/mnt/project/eggimasv/P4/P4_CH_NEU/425400', '/mnt/project/eggimasv/P4/P4_CH_NEU/428000', '/mnt/project/eggimasv/P4/P4_CH_NEU/432300', '/mnt/project/eggimasv/P4/P4_CH_NEU/43500', '/mnt/project/eggimasv/P4/P4_CH_NEU/441600', '/mnt/project/eggimasv/P4/P4_CH_NEU/442600', '/mnt/project/eggimasv/P4/P4_CH_NEU/455100', '/mnt/project/eggimasv/P4/P4_CH_NEU/469100', '/mnt/project/eggimasv/P4/P4_CH_NEU/483100', '/mnt/project/eggimasv/P4/P4_CH_NEU/483700', '/mnt/project/eggimasv/P4/P4_CH_NEU/49200', '/mnt/project/eggimasv/P4/P4_CH_NEU/500900', '/mnt/project/eggimasv/P4/P4_CH_NEU/509700', '/mnt/project/eggimasv/P4/P4_CH_NEU/511302', '/mnt/project/eggimasv/P4/P4_CH_NEU/515100', '/mnt/project/eggimasv/P4/P4_CH_NEU/518100', '/mnt/project/eggimasv/P4/P4_CH_NEU/526800', '/mnt/project/eggimasv/P4/P4_CH_NEU/528100', '/mnt/project/eggimasv/P4/P4_CH_NEU/541500', '/mnt/project/eggimasv/P4/P4_CH_NEU/542100', '/mnt/project/eggimasv/P4/P4_CH_NEU/542200', '/mnt/project/eggimasv/P4/P4_CH_NEU/542800', '/mnt/project/eggimasv/P4/P4_CH_NEU/543400', '/mnt/project/eggimasv/P4/P4_CH_NEU/547300', '/mnt/project/eggimasv/P4/P4_CH_NEU/548000', '/mnt/project/eggimasv/P4/P4_CH_NEU/548200', '/mnt/project/eggimasv/P4/P4_CH_NEU/549100', '/mnt/project/eggimasv/P4/P4_CH_NEU/549800', '/mnt/project/eggimasv/P4/P4_CH_NEU/550000', '/mnt/project/eggimasv/P4/P4_CH_NEU/551202', '/mnt/project/eggimasv/P4/P4_CH_NEU/551400', '/mnt/project/eggimasv/P4/P4_CH_NEU/551800', '/mnt/project/eggimasv/P4/P4_CH_NEU/565200', '/mnt/project/eggimasv/P4/P4_CH_NEU/565400', '/mnt/project/eggimasv/P4/P4_CH_NEU/56700', '/mnt/project/eggimasv/P4/P4_CH_NEU/567500', '/mnt/project/eggimasv/P4/P4_CH_NEU/570501', '/mnt/project/eggimasv/P4/P4_CH_NEU/57102', '/mnt/project/eggimasv/P4/P4_CH_NEU/57600', '/mnt/project/eggimasv/P4/P4_CH_NEU/581500', '/mnt/project/eggimasv/P4/P4_CH_NEU/58902', '/mnt/project/eggimasv/P4/P4_CH_NEU/642100', '/mnt/project/eggimasv/P4/P4_CH_NEU/645500', '/mnt/project/eggimasv/P4/P4_CH_NEU/645800', '/mnt/project/eggimasv/P4/P4_CH_NEU/650200', '/mnt/project/eggimasv/P4/P4_CH_NEU/6602', '/mnt/project/eggimasv/P4/P4_CH_NEU/664000', '/mnt/project/eggimasv/P4/P4_CH_NEU/664301', '/mnt/project/eggimasv/P4/P4_CH_NEU/664302', '/mnt/project/eggimasv/P4/P4_CH_NEU/66700', '/mnt/project/eggimasv/P4/P4_CH_NEU/67100', '/mnt/project/eggimasv/P4/P4_CH_NEU/671700', '/mnt/project/eggimasv/P4/P4_CH_NEU/674300', '/mnt/project/eggimasv/P4/P4_CH_NEU/675400', '/mnt/project/eggimasv/P4/P4_CH_NEU/677800', '/mnt/project/eggimasv/P4/P4_CH_NEU/678900', '/mnt/project/eggimasv/P4/P4_CH_NEU/679600', '/mnt/project/eggimasv/P4/P4_CH_NEU/69600', '/mnt/project/eggimasv/P4/P4_CH_NEU/701', '/mnt/project/eggimasv/P4/P4_CH_NEU/74600', '/mnt/project/eggimasv/P4/P4_CH_NEU/78200', '/mnt/project/eggimasv/P4/P4_CH_NEU/79100', '/mnt/project/eggimasv/P4/P4_CH_NEU/79400', '/mnt/project/eggimasv/P4/P4_CH_NEU/84301', '/mnt/project/eggimasv/P4/P4_CH_NEU/8901', '/mnt/project/eggimasv/P4/P4_CH_NEU/95200', '/mnt/project/eggimasv/P4/P4_CH_NEU/95600', '/mnt/project/eggimasv/P4/P4_CH_NEU/9601', '/mnt/project/eggimasv/P4/P4_CH_NEU/98123', '/mnt/project/eggimasv/P4/P4_CH_NEU/262200', '/mnt/project/eggimasv/P4/P4_CH_NEU/350601', '/mnt/project/eggimasv/P4/P4_CH_NEU/295100', '/mnt/project/eggimasv/P4/P4_CH_NEU/337600', '/mnt/project/eggimasv/P4/P4_CH_NEU/19201', '/mnt/project/eggimasv/P4/P4_CH_NEU/353101', '/mnt/project/eggimasv/P4/P4_CH_NEU/340200', '/mnt/project/eggimasv/P4/P4_CH_NEU/278800', '/mnt/project/eggimasv/P4/P4_CH_NEU/297100', '/mnt/project/eggimasv/P4/P4_CH_NEU/248000', '/mnt/project/eggimasv/P4/P4_CH_NEU/17701', '/mnt/project/eggimasv/P4/P4_CH_NEU/2801', '/mnt/project/eggimasv/P4/P4_CH_NEU/284100', '/mnt/project/eggimasv/P4/P4_CH_NEU/335200', '/mnt/project/eggimasv/P4/P4_CH_NEU/254400', '/mnt/project/eggimasv/P4/P4_CH_NEU/121100', '/mnt/project/eggimasv/P4/P4_CH_NEU/242900', '/mnt/project/eggimasv/P4/P4_CH_NEU/11701', '/mnt/project/eggimasv/P4/P4_CH_NEU/253400', '/mnt/project/eggimasv/P4/P4_CH_NEU/276600', '/mnt/project/eggimasv/P4/P4_CH_NEU/134400', '/mnt/project/eggimasv/P4/P4_CH_NEU/357301', '/mnt/project/eggimasv/P4/P4_CH_NEU/1001', '/mnt/project/eggimasv/P4/P4_CH_NEU/258300', '/mnt/project/eggimasv/P4/P4_CH_NEU/227400', '/mnt/project/eggimasv/P4/P4_CH_NEU/34500', '/mnt/project/eggimasv/P4/P4_CH_NEU/323700', '/mnt/project/eggimasv/P4/P4_CH_NEU/320302', '/mnt/project/eggimasv/P4/P4_CH_NEU/340500', '/mnt/project/eggimasv/P4/P4_CH_NEU/329200', '/mnt/project/eggimasv/P4/P4_CH_NEU/19601', '/mnt/project/eggimasv/P4/P4_CH_NEU/212400', '/mnt/project/eggimasv/P4/P4_CH_NEU/102300', '/mnt/project/eggimasv/P4/P4_CH_NEU/358201', '/mnt/project/eggimasv/P4/P4_CH_NEU/342500', '/mnt/project/eggimasv/P4/P4_CH_NEU/14001', '/mnt/project/eggimasv/P4/P4_CH_NEU/122000', '/mnt/project/eggimasv/P4/P4_CH_NEU/17401', '/mnt/project/eggimasv/P4/P4_CH_NEU/283100', '/mnt/project/eggimasv/P4/P4_CH_NEU/350602', '/mnt/project/eggimasv/P4/P4_CH_NEU/286100', '/mnt/project/eggimasv/P4/P4_CH_NEU/353201', '/mnt/project/eggimasv/P4/P4_CH_NEU/21101', '/mnt/project/eggimasv/P4/P4_CH_NEU/288700', '/mnt/project/eggimasv/P4/P4_CH_NEU/329800', '/mnt/project/eggimasv/P4/P4_CH_NEU/282300', '/mnt/project/eggimasv/P4/P4_CH_NEU/222800', '/mnt/project/eggimasv/P4/P4_CH_NEU/19801', '/mnt/project/eggimasv/P4/P4_CH_NEU/337200', '/mnt/project/eggimasv/P4/P4_CH_NEU/288100', '/mnt/project/eggimasv/P4/P4_CH_NEU/130103', '/mnt/project/eggimasv/P4/P4_CH_NEU/11501', '/mnt/project/eggimasv/P4/P4_CH_NEU/137100', '/mnt/project/eggimasv/P4/P4_CH_NEU/300102', '/mnt/project/eggimasv/P4/P4_CH_NEU/2501', '/mnt/project/eggimasv/P4/P4_CH_NEU/24201', '/mnt/project/eggimasv/P4/P4_CH_NEU/335702', '/mnt/project/eggimasv/P4/P4_CH_NEU/352301', '/mnt/project/eggimasv/P4/P4_CH_NEU/15401', '/mnt/project/eggimasv/P4/P4_CH_NEU/254200', '/mnt/project/eggimasv/P4/P4_CH_NEU/110400', '/mnt/project/eggimasv/P4/P4_CH_NEU/327100', '/mnt/project/eggimasv/P4/P4_CH_NEU/102400', '/mnt/project/eggimasv/P4/P4_CH_NEU/360501', '/mnt/project/eggimasv/P4/P4_CH_NEU/36200', '/mnt/project/eggimasv/P4/P4_CH_NEU/363201', '/mnt/project/eggimasv/P4/P4_CH_NEU/3701', '/mnt/project/eggimasv/P4/P4_CH_NEU/372201', '/mnt/project/eggimasv/P4/P4_CH_NEU/375201', '/mnt/project/eggimasv/P4/P4_CH_NEU/376201', '/mnt/project/eggimasv/P4/P4_CH_NEU/377501', '/mnt/project/eggimasv/P4/P4_CH_NEU/378801', '/mnt/project/eggimasv/P4/P4_CH_NEU/379001', '/mnt/project/eggimasv/P4/P4_CH_NEU/382201', '/mnt/project/eggimasv/P4/P4_CH_NEU/385102', '/mnt/project/eggimasv/P4/P4_CH_NEU/389101', '/mnt/project/eggimasv/P4/P4_CH_NEU/3901', '/mnt/project/eggimasv/P4/P4_CH_NEU/392101', '/mnt/project/eggimasv/P4/P4_CH_NEU/394201', '/mnt/project/eggimasv/P4/P4_CH_NEU/398101', '/mnt/project/eggimasv/P4/P4_CH_NEU/398302', '/mnt/project/eggimasv/P4/P4_CH_NEU/398601', '/mnt/project/eggimasv/P4/P4_CH_NEU/398701', '/mnt/project/eggimasv/P4/P4_CH_NEU/40100', '/mnt/project/eggimasv/P4/P4_CH_NEU/404200', '/mnt/project/eggimasv/P4/P4_CH_NEU/404300', '/mnt/project/eggimasv/P4/P4_CH_NEU/412300', '/mnt/project/eggimasv/P4/P4_CH_NEU/413500', '/mnt/project/eggimasv/P4/P4_CH_NEU/414500', '/mnt/project/eggimasv/P4/P4_CH_NEU/420600', '/mnt/project/eggimasv/P4/P4_CH_NEU/420800', '/mnt/project/eggimasv/P4/P4_CH_NEU/427100', '/mnt/project/eggimasv/P4/P4_CH_NEU/427600', '/mnt/project/eggimasv/P4/P4_CH_NEU/431100', '/mnt/project/eggimasv/P4/P4_CH_NEU/431300', '/mnt/project/eggimasv/P4/P4_CH_NEU/44400', '/mnt/project/eggimasv/P4/P4_CH_NEU/447100', '/mnt/project/eggimasv/P4/P4_CH_NEU/449700', '/mnt/project/eggimasv/P4/P4_CH_NEU/454200', '/mnt/project/eggimasv/P4/P4_CH_NEU/456600', '/mnt/project/eggimasv/P4/P4_CH_NEU/486400', '/mnt/project/eggimasv/P4/P4_CH_NEU/494600', '/mnt/project/eggimasv/P4/P4_CH_NEU/49602', '/mnt/project/eggimasv/P4/P4_CH_NEU/506100', '/mnt/project/eggimasv/P4/P4_CH_NEU/514700', '/mnt/project/eggimasv/P4/P4_CH_NEU/516300', '/mnt/project/eggimasv/P4/P4_CH_NEU/5201', '/mnt/project/eggimasv/P4/P4_CH_NEU/525500', '/mnt/project/eggimasv/P4/P4_CH_NEU/540500', '/mnt/project/eggimasv/P4/P4_CH_NEU/540700', '/mnt/project/eggimasv/P4/P4_CH_NEU/540900', '/mnt/project/eggimasv/P4/P4_CH_NEU/541001', '/mnt/project/eggimasv/P4/P4_CH_NEU/542300', '/mnt/project/eggimasv/P4/P4_CH_NEU/545100', '/mnt/project/eggimasv/P4/P4_CH_NEU/545600', '/mnt/project/eggimasv/P4/P4_CH_NEU/549200', '/mnt/project/eggimasv/P4/P4_CH_NEU/549602', '/mnt/project/eggimasv/P4/P4_CH_NEU/551900', '/mnt/project/eggimasv/P4/P4_CH_NEU/552001', '/mnt/project/eggimasv/P4/P4_CH_NEU/552701', '/mnt/project/eggimasv/P4/P4_CH_NEU/553300', '/mnt/project/eggimasv/P4/P4_CH_NEU/555100', '/mnt/project/eggimasv/P4/P4_CH_NEU/555500', '/mnt/project/eggimasv/P4/P4_CH_NEU/556600', '/mnt/project/eggimasv/P4/P4_CH_NEU/560200', '/mnt/project/eggimasv/P4/P4_CH_NEU/560401', '/mnt/project/eggimasv/P4/P4_CH_NEU/560402', '/mnt/project/eggimasv/P4/P4_CH_NEU/561101', '/mnt/project/eggimasv/P4/P4_CH_NEU/562200', '/mnt/project/eggimasv/P4/P4_CH_NEU/56300', '/mnt/project/eggimasv/P4/P4_CH_NEU/563900', '/mnt/project/eggimasv/P4/P4_CH_NEU/56500', '/mnt/project/eggimasv/P4/P4_CH_NEU/566100', '/mnt/project/eggimasv/P4/P4_CH_NEU/568500', '/mnt/project/eggimasv/P4/P4_CH_NEU/568900', '/mnt/project/eggimasv/P4/P4_CH_NEU/57500', '/mnt/project/eggimasv/P4/P4_CH_NEU/5801', '/mnt/project/eggimasv/P4/P4_CH_NEU/58200', '/mnt/project/eggimasv/P4/P4_CH_NEU/58400', '/mnt/project/eggimasv/P4/P4_CH_NEU/58800', '/mnt/project/eggimasv/P4/P4_CH_NEU/60800', '/mnt/project/eggimasv/P4/P4_CH_NEU/623300', '/mnt/project/eggimasv/P4/P4_CH_NEU/628900', '/mnt/project/eggimasv/P4/P4_CH_NEU/629300', '/mnt/project/eggimasv/P4/P4_CH_NEU/641300', '/mnt/project/eggimasv/P4/P4_CH_NEU/643100', '/mnt/project/eggimasv/P4/P4_CH_NEU/643700', '/mnt/project/eggimasv/P4/P4_CH_NEU/661100', '/mnt/project/eggimasv/P4/P4_CH_NEU/662002', '/mnt/project/eggimasv/P4/P4_CH_NEU/671800', '/mnt/project/eggimasv/P4/P4_CH_NEU/672200', '/mnt/project/eggimasv/P4/P4_CH_NEU/674201', '/mnt/project/eggimasv/P4/P4_CH_NEU/680400', '/mnt/project/eggimasv/P4/P4_CH_NEU/69000', '/mnt/project/eggimasv/P4/P4_CH_NEU/74000', '/mnt/project/eggimasv/P4/P4_CH_NEU/8301', '/mnt/project/eggimasv/P4/P4_CH_NEU/84300', '/mnt/project/eggimasv/P4/P4_CH_NEU/86900', '/mnt/project/eggimasv/P4/P4_CH_NEU/88500', '/mnt/project/eggimasv/P4/P4_CH_NEU/9401', '/mnt/project/eggimasv/P4/P4_CH_NEU/547900', '/mnt/project/eggimasv/P4/P4_CH_NEU/32101', '/mnt/project/eggimasv/P4/P4_CH_NEU/385103', '/mnt/project/eggimasv/P4/P4_CH_NEU/423700', '/mnt/project/eggimasv/P4/P4_CH_NEU/44600', '/mnt/project/eggimasv/P4/P4_CH_NEU/423500', '/mnt/project/eggimasv/P4/P4_CH_NEU/423600', '/mnt/project/eggimasv/P4/P4_CH_NEU/407500', '/mnt/project/eggimasv/P4/P4_CH_NEU/30800', '/mnt/project/eggimasv/P4/P4_CH_NEU/335601', '/mnt/project/eggimasv/P4/P4_CH_NEU/217300', '/mnt/project/eggimasv/P4/P4_CH_NEU/414100', '/mnt/project/eggimasv/P4/P4_CH_NEU/108300', '/mnt/project/eggimasv/P4/P4_CH_NEU/558600', '/mnt/project/eggimasv/P4/P4_CH_NEU/520300', '/mnt/project/eggimasv/P4/P4_CH_NEU/359401', '/mnt/project/eggimasv/P4/P4_CH_NEU/359501', '/mnt/project/eggimasv/P4/P4_CH_NEU/26101', '/mnt/project/eggimasv/P4/P4_CH_NEU/255500', '/mnt/project/eggimasv/P4/P4_CH_NEU/540200', '/mnt/project/eggimasv/P4/P4_CH_NEU/296400', '/mnt/project/eggimasv/P4/P4_CH_NEU/559000', '/mnt/project/eggimasv/P4/P4_CH_NEU/212700', '/mnt/project/eggimasv/P4/P4_CH_NEU/369301', '/mnt/project/eggimasv/P4/P4_CH_NEU/374301', '/mnt/project/eggimasv/P4/P4_CH_NEU/549601', '/mnt/project/eggimasv/P4/P4_CH_NEU/24301', '/mnt/project/eggimasv/P4/P4_CH_NEU/11201', '/mnt/project/eggimasv/P4/P4_CH_NEU/17102', '/mnt/project/eggimasv/P4/P4_CH_NEU/170500', '/mnt/project/eggimasv/P4/P4_CH_NEU/339100', '/mnt/project/eggimasv/P4/P4_CH_NEU/339200', '/mnt/project/eggimasv/P4/P4_CH_NEU/374601', '/mnt/project/eggimasv/P4/P4_CH_NEU/335400', '/mnt/project/eggimasv/P4/P4_CH_NEU/377601', '/mnt/project/eggimasv/P4/P4_CH_NEU/342200', '/mnt/project/eggimasv/P4/P4_CH_NEU/302501', '/mnt/project/eggimasv/P4/P4_CH_NEU/361201', '/mnt/project/eggimasv/P4/P4_CH_NEU/12101', '/mnt/project/eggimasv/P4/P4_CH_NEU/392401', '/mnt/project/eggimasv/P4/P4_CH_NEU/13801', '/mnt/project/eggimasv/P4/P4_CH_NEU/13301', '/mnt/project/eggimasv/P4/P4_CH_NEU/19301', '/mnt/project/eggimasv/P4/P4_CH_NEU/430300', '/mnt/project/eggimasv/P4/P4_CH_NEU/480100', '/mnt/project/eggimasv/P4/P4_CH_NEU/555300', '/mnt/project/eggimasv/P4/P4_CH_NEU/103300', '/mnt/project/eggimasv/P4/P4_CH_NEU/469600', '/mnt/project/eggimasv/P4/P4_CH_NEU/106902', '/mnt/project/eggimasv/P4/P4_CH_NEU/360602', '/mnt/project/eggimasv/P4/P4_CH_NEU/201300', '/mnt/project/eggimasv/P4/P4_CH_NEU/551300', '/mnt/project/eggimasv/P4/P4_CH_NEU/120800', '/mnt/project/eggimasv/P4/P4_CH_NEU/548600', '/mnt/project/eggimasv/P4/P4_CH_NEU/302301', '/mnt/project/eggimasv/P4/P4_CH_NEU/387101', '/mnt/project/eggimasv/P4/P4_CH_NEU/404100', '/mnt/project/eggimasv/P4/P4_CH_NEU/13201', '/mnt/project/eggimasv/P4/P4_CH_NEU/329404', '/mnt/project/eggimasv/P4/P4_CH_NEU/374101', '/mnt/project/eggimasv/P4/P4_CH_NEU/404400', '/mnt/project/eggimasv/P4/P4_CH_NEU/494100', '/mnt/project/eggimasv/P4/P4_CH_NEU/540100', '/mnt/project/eggimasv/P4/P4_CH_NEU/526200', '/mnt/project/eggimasv/P4/P4_CH_NEU/355101', '/mnt/project/eggimasv/P4/P4_CH_NEU/423900', '/mnt/project/eggimasv/P4/P4_CH_NEU/378902', '/mnt/project/eggimasv/P4/P4_CH_NEU/5501', '/mnt/project/eggimasv/P4/P4_CH_NEU/551500', '/mnt/project/eggimasv/P4/P4_CH_NEU/411400', '/mnt/project/eggimasv/P4/P4_CH_NEU/137000', '/mnt/project/eggimasv/P4/P4_CH_NEU/416900', '/mnt/project/eggimasv/P4/P4_CH_NEU/261801', '/mnt/project/eggimasv/P4/P4_CH_NEU/340603', '/mnt/project/eggimasv/P4/P4_CH_NEU/49700', '/mnt/project/eggimasv/P4/P4_CH_NEU/555600', '/mnt/project/eggimasv/P4/P4_CH_NEU/120401', '/mnt/project/eggimasv/P4/P4_CH_NEU/369401', '/mnt/project/eggimasv/P4/P4_CH_NEU/284400', '/mnt/project/eggimasv/P4/P4_CH_NEU/134600', '/mnt/project/eggimasv/P4/P4_CH_NEU/257800', '/mnt/project/eggimasv/P4/P4_CH_NEU/375101', '/mnt/project/eggimasv/P4/P4_CH_NEU/250200', '/mnt/project/eggimasv/P4/P4_CH_NEU/392701', '/mnt/project/eggimasv/P4/P4_CH_NEU/562400', '/mnt/project/eggimasv/P4/P4_CH_NEU/130101', '/mnt/project/eggimasv/P4/P4_CH_NEU/23001', '/mnt/project/eggimasv/P4/P4_CH_NEU/547100', '/mnt/project/eggimasv/P4/P4_CH_NEU/100100', '/mnt/project/eggimasv/P4/P4_CH_NEU/227900', '/mnt/project/eggimasv/P4/P4_CH_NEU/387102', '/mnt/project/eggimasv/P4/P4_CH_NEU/106500', '/mnt/project/eggimasv/P4/P4_CH_NEU/106700', '/mnt/project/eggimasv/P4/P4_CH_NEU/109800', '/mnt/project/eggimasv/P4/P4_CH_NEU/106603', '/mnt/project/eggimasv/P4/P4_CH_NEU/221900', '/mnt/project/eggimasv/P4/P4_CH_NEU/140200', '/mnt/project/eggimasv/P4/P4_CH_NEU/131102', '/mnt/project/eggimasv/P4/P4_CH_NEU/10001', '/mnt/project/eggimasv/P4/P4_CH_NEU/300501', '/mnt/project/eggimasv/P4/P4_CH_NEU/507900', '/mnt/project/eggimasv/P4/P4_CH_NEU/310100', '/mnt/project/eggimasv/P4/P4_CH_NEU/15501', '/mnt/project/eggimasv/P4/P4_CH_NEU/459100', '/mnt/project/eggimasv/P4/P4_CH_NEU/406300', '/mnt/project/eggimasv/P4/P4_CH_NEU/377502', '/mnt/project/eggimasv/P4/P4_CH_NEU/11301', '/mnt/project/eggimasv/P4/P4_CH_NEU/463500', '/mnt/project/eggimasv/P4/P4_CH_NEU/342600', '/mnt/project/eggimasv/P4/P4_CH_NEU/398202', '/mnt/project/eggimasv/P4/P4_CH_NEU/541300', '/mnt/project/eggimasv/P4/P4_CH_NEU/541200', '/mnt/project/eggimasv/P4/P4_CH_NEU/245400', '/mnt/project/eggimasv/P4/P4_CH_NEU/300700', '/mnt/project/eggimasv/P4/P4_CH_NEU/121500', '/mnt/project/eggimasv/P4/P4_CH_NEU/120600', '/mnt/project/eggimasv/P4/P4_CH_NEU/430700', '/mnt/project/eggimasv/P4/P4_CH_NEU/511400', '/mnt/project/eggimasv/P4/P4_CH_NEU/404700', '/mnt/project/eggimasv/P4/P4_CH_NEU/202900', '/mnt/project/eggimasv/P4/P4_CH_NEU/220200', '/mnt/project/eggimasv/P4/P4_CH_NEU/373401', '/mnt/project/eggimasv/P4/P4_CH_NEU/100401', '/mnt/project/eggimasv/P4/P4_CH_NEU/419800', '/mnt/project/eggimasv/P4/P4_CH_NEU/121200', '/mnt/project/eggimasv/P4/P4_CH_NEU/286001', '/mnt/project/eggimasv/P4/P4_CH_NEU/430900', '/mnt/project/eggimasv/P4/P4_CH_NEU/453400', '/mnt/project/eggimasv/P4/P4_CH_NEU/564200', '/mnt/project/eggimasv/P4/P4_CH_NEU/564400', '/mnt/project/eggimasv/P4/P4_CH_NEU/571700', '/mnt/project/eggimasv/P4/P4_CH_NEU/57400', '/mnt/project/eggimasv/P4/P4_CH_NEU/59300', '/mnt/project/eggimasv/P4/P4_CH_NEU/61600', '/mnt/project/eggimasv/P4/P4_CH_NEU/626603', '/mnt/project/eggimasv/P4/P4_CH_NEU/628300', '/mnt/project/eggimasv/P4/P4_CH_NEU/628500', '/mnt/project/eggimasv/P4/P4_CH_NEU/628700', '/mnt/project/eggimasv/P4/P4_CH_NEU/629200', '/mnt/project/eggimasv/P4/P4_CH_NEU/630000', '/mnt/project/eggimasv/P4/P4_CH_NEU/640400', '/mnt/project/eggimasv/P4/P4_CH_NEU/640600', '/mnt/project/eggimasv/P4/P4_CH_NEU/641402', '/mnt/project/eggimasv/P4/P4_CH_NEU/642300', '/mnt/project/eggimasv/P4/P4_CH_NEU/643200', '/mnt/project/eggimasv/P4/P4_CH_NEU/643600', '/mnt/project/eggimasv/P4/P4_CH_NEU/645700', '/mnt/project/eggimasv/P4/P4_CH_NEU/651000', '/mnt/project/eggimasv/P4/P4_CH_NEU/670900', '/mnt/project/eggimasv/P4/P4_CH_NEU/675000', '/mnt/project/eggimasv/P4/P4_CH_NEU/675100', '/mnt/project/eggimasv/P4/P4_CH_NEU/680000', '/mnt/project/eggimasv/P4/P4_CH_NEU/6801', '/mnt/project/eggimasv/P4/P4_CH_NEU/72200', '/mnt/project/eggimasv/P4/P4_CH_NEU/75100', '/mnt/project/eggimasv/P4/P4_CH_NEU/78500', '/mnt/project/eggimasv/P4/P4_CH_NEU/94400', '/mnt/project/eggimasv/P4/P4_CH_NEU/44800', '/mnt/project/eggimasv/P4/P4_CH_NEU/200400', '/mnt/project/eggimasv/P4/P4_CH_NEU/375301', '/mnt/project/eggimasv/P4/P4_CH_NEU/340301', '/mnt/project/eggimasv/P4/P4_CH_NEU/19101', '/mnt/project/eggimasv/P4/P4_CH_NEU/270101', '/mnt/project/eggimasv/P4/P4_CH_NEU/325400', '/mnt/project/eggimasv/P4/P4_CH_NEU/390101', '/mnt/project/eggimasv/P4/P4_CH_NEU/511301', '/mnt/project/eggimasv/P4/P4_CH_NEU/220600', '/mnt/project/eggimasv/P4/P4_CH_NEU/289100', '/mnt/project/eggimasv/P4/P4_CH_NEU/56102', '/mnt/project/eggimasv/P4/P4_CH_NEU/170200', '/mnt/project/eggimasv/P4/P4_CH_NEU/647600', '/mnt/project/eggimasv/P4/P4_CH_NEU/549900', '/mnt/project/eggimasv/P4/P4_CH_NEU/41100', '/mnt/project/eggimasv/P4/P4_CH_NEU/32300', '/mnt/project/eggimasv/P4/P4_CH_NEU/401', '/mnt/project/eggimasv/P4/P4_CH_NEU/61100', '/mnt/project/eggimasv/P4/P4_CH_NEU/120400', '/mnt/project/eggimasv/P4/P4_CH_NEU/3801', '/mnt/project/eggimasv/P4/P4_CH_NEU/262100', '/mnt/project/eggimasv/P4/P4_CH_NEU/329100', '/mnt/project/eggimasv/P4/P4_CH_NEU/250100', '/mnt/project/eggimasv/P4/P4_CH_NEU/331200', '/mnt/project/eggimasv/P4/P4_CH_NEU/209600', '/mnt/project/eggimasv/P4/P4_CH_NEU/15601', '/mnt/project/eggimasv/P4/P4_CH_NEU/286500', '/mnt/project/eggimasv/P4/P4_CH_NEU/500500', '/mnt/project/eggimasv/P4/P4_CH_NEU/568200', '/mnt/project/eggimasv/P4/P4_CH_NEU/15301', '/mnt/project/eggimasv/P4/P4_CH_NEU/160600', '/mnt/project/eggimasv/P4/P4_CH_NEU/5301', '/mnt/project/eggimasv/P4/P4_CH_NEU/329600', '/mnt/project/eggimasv/P4/P4_CH_NEU/277500', '/mnt/project/eggimasv/P4/P4_CH_NEU/245700', '/mnt/project/eggimasv/P4/P4_CH_NEU/414400', '/mnt/project/eggimasv/P4/P4_CH_NEU/560600', '/mnt/project/eggimasv/P4/P4_CH_NEU/541002', '/mnt/project/eggimasv/P4/P4_CH_NEU/36000', '/mnt/project/eggimasv/P4/P4_CH_NEU/11801', '/mnt/project/eggimasv/P4/P4_CH_NEU/293700', '/mnt/project/eggimasv/P4/P4_CH_NEU/553000', '/mnt/project/eggimasv/P4/P4_CH_NEU/121700', '/mnt/project/eggimasv/P4/P4_CH_NEU/15801', '/mnt/project/eggimasv/P4/P4_CH_NEU/374401', '/mnt/project/eggimasv/P4/P4_CH_NEU/22401', '/mnt/project/eggimasv/P4/P4_CH_NEU/542500', '/mnt/project/eggimasv/P4/P4_CH_NEU/19501', '/mnt/project/eggimasv/P4/P4_CH_NEU/351501', '/mnt/project/eggimasv/P4/P4_CH_NEU/220000', '/mnt/project/eggimasv/P4/P4_CH_NEU/320401', '/mnt/project/eggimasv/P4/P4_CH_NEU/420300', '/mnt/project/eggimasv/P4/P4_CH_NEU/553900', '/mnt/project/eggimasv/P4/P4_CH_NEU/113400', '/mnt/project/eggimasv/P4/P4_CH_NEU/443600', '/mnt/project/eggimasv/P4/P4_CH_NEU/285500', '/mnt/project/eggimasv/P4/P4_CH_NEU/391101', '/mnt/project/eggimasv/P4/P4_CH_NEU/571900', '/mnt/project/eggimasv/P4/P4_CH_NEU/247801', '/mnt/project/eggimasv/P4/P4_CH_NEU/100900', '/mnt/project/eggimasv/P4/P4_CH_NEU/427200', '/mnt/project/eggimasv/P4/P4_CH_NEU/660301', '/mnt/project/eggimasv/P4/P4_CH_NEU/571200', '/mnt/project/eggimasv/P4/P4_CH_NEU/137200', '/mnt/project/eggimasv/P4/P4_CH_NEU/423400', '/mnt/project/eggimasv/P4/P4_CH_NEU/556500', '/mnt/project/eggimasv/P4/P4_CH_NEU/21801', '/mnt/project/eggimasv/P4/P4_CH_NEU/380501', '/mnt/project/eggimasv/P4/P4_CH_NEU/571300', '/mnt/project/eggimasv/P4/P4_CH_NEU/329300', '/mnt/project/eggimasv/P4/P4_CH_NEU/4201', '/mnt/project/eggimasv/P4/P4_CH_NEU/288300', '/mnt/project/eggimasv/P4/P4_CH_NEU/359201', '/mnt/project/eggimasv/P4/P4_CH_NEU/517800', '/mnt/project/eggimasv/P4/P4_CH_NEU/640200', '/mnt/project/eggimasv/P4/P4_CH_NEU/552702', '/mnt/project/eggimasv/P4/P4_CH_NEU/303401', '/mnt/project/eggimasv/P4/P4_CH_NEU/661900', '/mnt/project/eggimasv/P4/P4_CH_NEU/545200', '/mnt/project/eggimasv/P4/P4_CH_NEU/378201', '/mnt/project/eggimasv/P4/P4_CH_NEU/170400', '/mnt/project/eggimasv/P4/P4_CH_NEU/279300', '/mnt/project/eggimasv/P4/P4_CH_NEU/293800', '/mnt/project/eggimasv/P4/P4_CH_NEU/12001', '/mnt/project/eggimasv/P4/P4_CH_NEU/17101', '/mnt/project/eggimasv/P4/P4_CH_NEU/337700', '/mnt/project/eggimasv/P4/P4_CH_NEU/249200', '/mnt/project/eggimasv/P4/P4_CH_NEU/26102', '/mnt/project/eggimasv/P4/P4_CH_NEU/21701', '/mnt/project/eggimasv/P4/P4_CH_NEU/60700', '/mnt/project/eggimasv/P4/P4_CH_NEU/361401', '/mnt/project/eggimasv/P4/P4_CH_NEU/425800', '/mnt/project/eggimasv/P4/P4_CH_NEU/474600', '/mnt/project/eggimasv/P4/P4_CH_NEU/411800', '/mnt/project/eggimasv/P4/P4_CH_NEU/548700', '/mnt/project/eggimasv/P4/P4_CH_NEU/403000', '/mnt/project/eggimasv/P4/P4_CH_NEU/140400', '/mnt/project/eggimasv/P4/P4_CH_NEU/323100', '/mnt/project/eggimasv/P4/P4_CH_NEU/563000', '/mnt/project/eggimasv/P4/P4_CH_NEU/412100', '/mnt/project/eggimasv/P4/P4_CH_NEU/547400', '/mnt/project/eggimasv/P4/P4_CH_NEU/663801', '/mnt/project/eggimasv/P4/P4_CH_NEU/397201', '/mnt/project/eggimasv/P4/P4_CH_NEU/551600', '/mnt/project/eggimasv/P4/P4_CH_NEU/160200', '/mnt/project/eggimasv/P4/P4_CH_NEU/504300', '/mnt/project/eggimasv/P4/P4_CH_NEU/403300', '/mnt/project/eggimasv/P4/P4_CH_NEU/224300', '/mnt/project/eggimasv/P4/P4_CH_NEU/641401', '/mnt/project/eggimasv/P4/P4_CH_NEU/650800', '/mnt/project/eggimasv/P4/P4_CH_NEU/541100', '/mnt/project/eggimasv/P4/P4_CH_NEU/384301', '/mnt/project/eggimasv/P4/P4_CH_NEU/564600', '/mnt/project/eggimasv/P4/P4_CH_NEU/150900', '/mnt/project/eggimasv/P4/P4_CH_NEU/282500', '/mnt/project/eggimasv/P4/P4_CH_NEU/247900', '/mnt/project/eggimasv/P4/P4_CH_NEU/626601', '/mnt/project/eggimasv/P4/P4_CH_NEU/284700', '/mnt/project/eggimasv/P4/P4_CH_NEU/325100', '/mnt/project/eggimasv/P4/P4_CH_NEU/21901', '/mnt/project/eggimasv/P4/P4_CH_NEU/218400', '/mnt/project/eggimasv/P4/P4_CH_NEU/57300', '/mnt/project/eggimasv/P4/P4_CH_NEU/120101', '/mnt/project/eggimasv/P4/P4_CH_NEU/201', '/mnt/project/eggimasv/P4/P4_CH_NEU/570800', '/mnt/project/eggimasv/P4/P4_CH_NEU/15802', '/mnt/project/eggimasv/P4/P4_CH_NEU/432100', '/mnt/project/eggimasv/P4/P4_CH_NEU/60400', '/mnt/project/eggimasv/P4/P4_CH_NEU/671900', '/mnt/project/eggimasv/P4/P4_CH_NEU/675700', '/mnt/project/eggimasv/P4/P4_CH_NEU/677500', '/mnt/project/eggimasv/P4/P4_CH_NEU/679300', '/mnt/project/eggimasv/P4/P4_CH_NEU/70400', '/mnt/project/eggimasv/P4/P4_CH_NEU/71001', '/mnt/project/eggimasv/P4/P4_CH_NEU/72500', '/mnt/project/eggimasv/P4/P4_CH_NEU/73300', '/mnt/project/eggimasv/P4/P4_CH_NEU/78400', '/mnt/project/eggimasv/P4/P4_CH_NEU/90200', '/mnt/project/eggimasv/P4/P4_CH_NEU/90600', '/mnt/project/eggimasv/P4/P4_CH_NEU/92402', '/mnt/project/eggimasv/P4/P4_CH_NEU/99200', '/mnt/project/eggimasv/P4/P4_CH_NEU/99400']


def getClusterPos(a, position):
    cnt = 0
    for FolderPath in a:
        getNR = FolderPath.split("/mnt/project/eggimasv/P4/P4_CH_NEU/") #"CALCULATION_P4_CH_NEU")
        ARA_NR = int(getNR[1][:])
        if ARA_NR == position:
            print cnt
            return
        cnt += 1

#----------

import os
import glob
import arcpy
import numpy
import sys
    
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

def collectDataAllRuns(path):
    '''
    Collects 
    '''
    # List with all results from all the calculations
    resultFolder = []
    
    # Get the folders
    folderList = os.listdir(path) 
    for folder in folderList:
        resultFolder.append(path[:-1] + folder)

    return resultFolder

def readLines(pathInFile):
    """
    This functions reads out lines of a .txt file
    
    Input Arguments: 
    pathInFile       --    Path to .txt file
    
    Output Arguments:
    readLines        --      Statistics
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    readLines = []                      # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
        entry = lineArray[position]     # Get line at position
        readLines.append(entry)         # Append line at position to empty List
        position += 1                   # For the loop
    inputfile.close()                   # Close result .txt file 
    return readLines


def readInWWTPs(pathInFile):
    """
    This functions reads in a .txt file.
    
    Input Arguments: 
    pathInFile           --    Path to .txt file
    
    Output Arguments:
    liste                --   List with edges
    """
    txtFileList = readLines(pathInFile)
    liste = []
    # Read out only string
    for i in txtFileList[:-1]:
        _ = i.split(",", 2)
        ID = int(_[0][1:])
        flow = float(_[1][1:-2])
        liste.append([ID, flow])               # append who line
    return liste


def calculateTotalWWTPSUM(WWTPS, EW_Q):
    
    # This functions sums total PE
    
    totalFlow = 0
    
    for i in WWTPS:
        totalFlow += i[1]
        
    totalPE = totalFlow/EW_Q
    
    return totalPE


def getPercentagesWWTP(WWTPS, EW_Q, sizeSmallWWTP, sizeMiddleWWTP):
    
    # Calculates percentages of each WWTP Distribution
    small, middle, large = 0, 0, 0
    totalPE = calculateTotalWWTPSUM(WWTPS, EW_Q)

    for i in WWTPS:
        PE = i[1]/float(EW_Q)
        if PE <= sizeSmallWWTP:
            small += PE
        if PE > sizeSmallWWTP and PE <= sizeMiddleWWTP:
            middle += PE
        if PE > sizeMiddleWWTP:
            large += PE
    
    # Percentages are given in % ..> 0,05 --> 5 %
    if small > 0:
        percentageSmallWWTP = ((100.0/float(totalPE))*small) / 100.0
    else:
        percentageSmallWWTP = 0.0
    
    if middle > 0:
        percentageMiddle = ((100.0/float(totalPE))*middle) / 100.0
    else:
        percentageMiddle = 0
    
    if large > 0:
        percentageLarge = ((100.0/float(totalPE))*large) / 100.0
    else:
        percentageLarge = 0
    
    return totalPE, percentageSmallWWTP, percentageMiddle, percentageLarge

def readStatistics(pathInFile):
    """
    This functions reads out statistical data from a .txt file
    
    Input Arguments: 
    pathInFile        --    Path to .txt file
    
    Output Arguments:
    statistics        --      Statistics
    """
    inputfile = open(pathInFile, 'r')   # Set Path to existing .txt-File with R results
    lineArray = inputfile.readlines()   # Read in single result lines from txtfile into List
    lines = []                          # Create empty list to fill in whole txt File with results
    position = 0                        
    while position < len(lineArray):    # Iterate through list with line-results by position
        entry = lineArray[position]     # Get line at position
        lines.append(entry)             # Append line at position to empty List
        position += 1                   # For the loop
    inputfile.close()                   # Close result .txt file 

    id_Startnode = float(lines[0])
    sources = float(lines[1][:-1])
    sinks = float(lines[2][:-1])
    degCen = float(lines[3][:-1])
    degCenWeighted = float(lines[4][:-1])  
    nrOfNeighboursDensity = float(lines[5][:-1])
    totalPipeLength = float(lines[6][:-1])   
    avreageTrenchDepth = float(lines[7][:-1])   
    averageHeight = float(lines[8][:-1])   
    averageWWTPSize = float(lines[9][:-1])   
    medianWWTOSize = float(lines[10][:-1])   
    completePumpCosts = float(lines[15][:-1])
    completeWWTPCosts = float(lines[16][:-1])
    completePublicPipeCosts = float(lines[17][:-1])
    totCostPrivateSewer = float(lines[18][:-1])
    totSystemCostsNoPrivate = float(lines[19][:-1])
    totSystemCostsWithPrivate = float(lines[20])

    statistics = [id_Startnode, sources, sinks, degCen, degCenWeighted, nrOfNeighboursDensity, totalPipeLength, avreageTrenchDepth, averageHeight, averageWWTPSize, medianWWTOSize, 
                  completePumpCosts, completeWWTPCosts, completePublicPipeCosts, totCostPrivateSewer, totSystemCostsNoPrivate, totSystemCostsWithPrivate]
    return statistics



def readInGeoDictionary(pathInFile):
    """
    This functions reads out statistical data from a .txt file
    
    Input Arguments: 
    pathInFile        --    Path to .txt file
    
    Output Arguments:
    statistics        --      Statistics
    """
    
    txtFileList = readLines(pathInFile)
    
    # Add first element
    catchements = []

    for g in txtFileList:
        f = g.split(",", 3)
        #print(f)
        #print(int(f[0][1:]))
        #print(int(f[1][1:-1]))
        #print(str(f[2][2:-1]))
        catchements.append([int(f[0][1:]), int(f[1]), str(f[2][1:-1])])
    
    '''
    
    # Add first element
    catchements = []
    firstEntry= txtFileList[0]
    
    f = firstEntry.split(",", 4)
    catchements.append([int(f[0][2:]), int(f[1]), str(f[2][1:-1]), int(f[3]), str(f[4][1:-4])])

    #print("A: " + str(catchements))

    for f in txtFileList[1:]:
        g = f.split(",", 4)
        #print("g: " + str(g))
        
        catchements.append([int(g[0][1:]), int(g[1]), str(g[2][1:-1]), int(g[3]), str(g[4][1:-4])])
        #print(catchements)
        #print"---"
    '''

    return catchements # KT_NR, ARA_Nr, ARA_Name

def readInARETypologieDictionary(pathInFile):
    """
    """
    
    txtFileList = readLines(pathInFile)
    catchements = []
    for i in txtFileList:
        # Add first element
        
        f = i.split(",", 4)
        catchements.append([int(f[0][1:]), str(f[1][1:-1]), int(f[2]), int(f[3][:-1])])
        
    return catchements



def getDensitiesCatchement(pathExtent_gem, pathBuildings_inhabited, pathSettArea, FISHNET):
    
    totSettlmentArea, totCatchmentArea, totPop = 0, 0, 0
    
    # Read in total Area & population
    if FISHNET == False:
        settlementAreaRows = arcpy.da.SearchCursor(pathExtent_gem, ["Shape_Area"])    
        for i in settlementAreaRows:
            totCatchmentArea = i[0]
    else:
        totCatchmentArea = 7200 * 7200 # [m2]
        
    buildlingPop = arcpy.da.SearchCursor(pathBuildings_inhabited, ["Pop_Build"])    
    for i in buildlingPop:
        totPop += i[0]
    
    # Read in Settlement Area
    settlementAreaRows = arcpy.da.SearchCursor(pathSettArea, ["AREA"])    
    for i in settlementAreaRows:
        totSettlmentArea += i[0]
    
    #print("totCatchmentArea: " + str(totCatchmentArea))
    #print("totPop: " + str(totPop))
    #print("totSettlmentArea: " + str(totSettlmentArea))  
    
    # Todo --> Think what if settlment area is zerO!  
    regularPopulationDensity = totPop / float(totCatchmentArea/1000000) # Person / km2
    if totSettlmentArea > 0:
        NeighborhoodDensity = totPop / float(totSettlmentArea/1000000)
    else:
        # if no settlement area, assume very low settlemetn area 
        NeighborhoodDensity = regularPopulationDensity
        
    return regularPopulationDensity, NeighborhoodDensity, totCatchmentArea, totPop, totSettlmentArea



def assignCatchementsToCanton(catchmentDictionaryNotSorted, kantonGeoBFS):
    
    # This function attributes the catchement to one canton depending on the number of communities
    # only community is returned per catchement
    
    # Catchmenet Number, Canton Number with Dominant Area
    catchmenetsCanton = [[500500, 21], [329100, 18], [329501, 17], [160200, 8], [333800, 17], [170200, 9], [269400, 20], [42800, 19], [414100, 3], [34500, 3], [400100, 19], [427600, 19], [427100, 19], [283100, 11], [270101, 12], [253400, 2], [245700, 2], [254600, 2], [66700, 2], [226500, 10], [227400, 10], [201300, 10], [23100, 10], [581500, 22], [571700, 25]]
    
    
    catchmentPerCanton = []
    checkedCatchementNr = []
    
    
    
    #for community in catchmentDictionaryNotSorted:

    #catchmentPerCanton
    
    
    def most_common(lst):
        return max(set(lst), key=lst.count)

    '''for i in catchmentDictionaryNotSorted:
        print("ENTRY: ---------------------: " + str(i))
        #print("len(catchmentPerCanton: " + str(len(catchmentPerCanton)))
        #print("len(checkedCatchementNr): " + str(len(checkedCatchementNr)))
        #print(checkedCatchementNr)
        ARA_NR = i[3]
        listWithSameARANR, WWTPcommunities = [], []
        
        if ARA_NR not in checkedCatchementNr:
            mostCommonKT = "None"
            
            # Check whether in Special Canton List
            for Catch in catchmenetsCanton:
                if Catch[0] == ARA_NR:
                    mostCommonKTShort = Catch[1]
                    
                    for numb in kantonGeoBFS:
                        if mostCommonKTShort == numb[0]:
                            mostCommonKT = numb[2]
                            print("mostCommonKT: " + str(mostCommonKT))
                            break
                    #print("Catchemnet crosses cantons: " + str(ARA_NR))
                    #print("mostCommonKTShort: " + str(mostCommonKTShort))
                    #print("mostCommonKT: " + str(mostCommonKT))
                    break
            
            # If not in dictionary with crossing WWTP catchements, take regular canton number
            if mostCommonKT == "None":
                print("Not across Cnatons")
                mostCommonKT = i[1]
                
            for e in catchmentDictionaryNotSorted:
                if e[3] == ARA_NR:
                    WWTPcommunities.append(e)
                
            #print("Len WWTPcommunities: " + str(len(WWTPcommunities)))    
            for f in WWTPcommunities:
                if f[1] == mostCommonKT:
                    catchmentPerCanton.append(f)
                    #print("add")
                    break
            print("ARA_NR: " + str(ARA_NR))
            checkedCatchementNr.append(ARA_NR)
            #print("len checkedCatchementNr: " + str(len(checkedCatchementNr)))
        else:
            _ = 0
            print "Already added Catchement"
            
    '''
            
    '''
            for e in catchmentDictionaryNotSorted:
                if e[3] == ARA_NR:
                    listWithSameARANR.append(e[1]) # ADd Canton
                    WWTPcommunities.append(e)
            mostCommonKT = most_common(listWithSameARANR) # Get most often canton
            '''
            
    '''# ASsign the first catchement of this canton
        for f in WWTPcommunities:
            if f[1] == mostCommonKT:
                catchmentPerCanton.append(f)
                break
        checkedCatchementNr.append(ARA_NR)
    '''
    return catchmentPerCanton

# --------------------
# Input Paramters
# --------------------
kantonGeoBFS = [[1, 'Zurich', 'ZH'], [2, 'Bern', 'BE'], [3, 'Luzern', 'LU'], [4, 'Uri', 'UR'], [5, 'Schwyz', 'SZ'], [6, 'Obwalden', 'OW'], [7, 'Nidwalden', 'NW'], [8, 'Glarus', 'GL'], [9, 'Zug', 'ZG'], [10, 'Freiburg', 'FR'], [11, 'Solothurn', 'SO'], [12, 'Basel-Stadt', 'BS'], [13, 'Basel-Landschaft', 'BL'], [14, 'Schaffhausen', 'SH'], [15, 'Appenzell Ausserrhoden', 'AR'], [16, 'Appenzell Innerrhoden', 'AI'], [17, 'St. Gallen', 'SG'], [18, 'Graubuenden', 'GR'], [19, 'Aargau', 'AG'], [20, 'Thurgau', 'TG'], [21, 'Tessin', 'TI'], [22, 'Waadt', 'VD'], [23, 'Wallis', 'VS'], [24, 'Neuenburg', 'NE'], [25, 'Genf','GE'], [26, 'Jura', 'JU']]


FISHNET = False

if FISHNET == False:
    FolderPath = r'P4_CH_SNIP_CALCULATED'
    pathResultFolder    = r'C:\\' + FolderPath + r'\\' # r'C:\\_SCRAP_FOLDERSTRUCTURE\\'  # Is the same as in datPerparatorCHF the main folder 
else:
    FolderPath = r'P4_FISHNET_RESULT'
    pathResultFolder    = r'F:\\' + FolderPath + r'\\'
    
    # ID, KT_ID
    dictionaryFishNet = [[31, 21], [32, 21], [33, 21], [80, 21], [81, 21], [82, 21], [116, 23], [117, 23], [128, 21], [129, 21], [130, 21], [166, 23], [178, 21], [179, 21], [180, 21], [213, 23], [214, 23], [215, 23], [217, 23], [225, 21], [226, 21], [227, 21], [228, 21], [229, 21], [245, 25], [246, 25], [247, 25], [259, 23], [260, 23], [262, 23], [264, 23], [265, 23], [266, 23], [273, 21], [274, 21], [275, 21], [276, 21], [277, 21], [278, 21], [279, 18], [294, 25], [295, 25], [296, 25], [297, 25], [304, 23], [305, 22], [306, 22], [308, 23], [309, 23], [311, 23], [314, 23], [322, 21], [323, 21], [324, 21], [325, 21], [326, 21], [327, 18], [328, 18], [338, 18], [344, 25], [345, 22], [353, 23], [354, 22], [355, 22], [358, 23], [371, 21], [372, 21], [373, 21], [374, 21], [375, 21], [377, 18], [386, 18], [387, 18], [394, 22], [401, 23], [402, 22], [403, 22], [404, 22], [405, 2], [406, 2], [407, 2], [408, 2], [419, 21], [420, 21], [423, 21], [424, 21], [425, 21], [426, 18], [427, 18], [430, 18], [431, 18], [435, 18], [436, 18], [442, 22], [443, 22], [451, 22], [452, 22], [454, 22], [455, 2], [456, 2], [457, 2], [458, 2], [459, 2], [460, 2], [472, 21], [475, 18], [476, 18], [480, 18], [481, 18], [482, 18], [483, 18], [484, 18], [493, 22], [494, 22], [495, 22], [496, 22], [497, 22], [498, 22], [501, 10], [502, 10], [503, 22], [504, 2], [505, 2], [506, 2], [507, 2], [508, 2], [509, 2], [510, 2], [517, 21], [518, 21], [519, 21], [520, 21], [521, 21], [524, 18], [526, 18], [529, 18], [530, 18], [531, 18], [532, 18], [533, 18], [543, 22], [544, 22], [545, 22], [546, 22], [547, 22], [549, 10], [550, 10], [551, 10], [552, 10], [553, 2], [554, 2], [555, 2], [556, 2], [557, 2], [558, 2], [559, 2], [560, 2], [566, 21], [567, 21], [568, 21], [569, 18], [570, 21], [571, 21], [572, 18], [573, 18], [574, 18], [575, 18], [576, 18], [577, 18], [578, 18], [580, 18], [581, 18], [586, 18], [592, 22], [593, 22], [594, 22], [595, 22], [596, 22], [597, 10], [598, 10], [599, 10], [600, 10], [601, 10], [602, 10], [603, 2], [604, 2], [605, 2], [606, 2], [607, 2], [608, 2], [609, 2], [610, 2], [612, 2], [613, 2], [614, 4], [615, 4], [616, 4], [617, 18], [618, 18], [619, 18], [621, 18], [622, 18], [624, 18], [625, 18], [626, 18], [627, 18], [628, 18], [629, 18], [630, 18], [631, 18], [634, 18], [635, 18], [641, 22], [642, 22], [643, 22], [644, 22], [645, 22], [646, 22], [647, 10], [648, 10], [649, 10], [650, 10], [651, 10], [652, 2], [653, 2], [654, 2], [655, 2], [656, 2], [657, 2], [658, 2], [659, 2], [660, 2], [661, 2], [662, 2], [663, 2], [664, 4], [665, 4], [666, 18], [667, 18], [668, 18], [669, 18], [670, 18], [671, 18], [673, 18], [674, 18], [675, 18], [676, 18], [677, 18], [680, 18], [681, 18], [683, 18], [693, 22], [694, 22], [695, 22], [696, 22], [697, 10], [698, 10], [699, 10], [700, 2], [701, 2], [702, 2], [703, 2], [704, 2], [705, 2], [706, 2], [707, 2], [708, 2], [709, 6], [710, 2], [711, 2], [712, 2], [713, 4], [714, 4], [715, 4], [717, 18], [718, 18], [719, 18], [720, 18], [721, 18], [722, 18], [723, 18], [724, 18], [725, 18], [726, 18], [727, 18], [728, 18], [729, 18], [730, 18], [732, 18], [740, 22], [742, 22], [743, 22], [744, 10], [745, 22], [746, 10], [747, 10], [748, 10], [749, 10], [750, 2], [751, 2], [752, 2], [753, 2], [754, 2], [755, 2], [756, 3], [757, 6], [758, 6], [759, 6], [760, 7], [761, 6], [762, 4], [763, 4], [764, 4], [766, 8], [767, 8], [768, 18], [769, 18], [770, 18], [771, 18], [772, 18], [773, 18], [774, 18], [775, 18], [776, 18], [777, 18], [779, 18], [780, 18], [781, 18], [789, 24], [790, 24], [791, 22], [792, 22], [793, 22], [794, 10], [795, 22], [796, 10], [797, 10], [798, 2], [799, 2], [800, 2], [801, 2], [802, 2], [803, 2], [804, 2], [805, 3], [806, 3], [807, 6], [808, 6], [809, 7], [810, 7], [811, 4], [812, 4], [813, 4], [814, 4], [815, 4], [816, 8], [817, 8], [818, 8], [819, 18], [820, 18], [821, 18], [822, 18], [823, 18], [824, 18], [825, 18], [826, 18], [830, 18], [831, 18], [839, 24], [840, 24], [841, 24], [842, 24], [843, 22], [844, 22], [845, 10], [846, 2], [847, 2], [848, 2], [849, 2], [850, 2], [851, 2], [852, 2], [853, 2], [854, 3], [855, 3], [856, 6], [857, 6], [858, 7], [859, 7], [860, 7], [861, 5], [862, 5], [863, 5], [864, 5], [865, 8], [866, 8], [867, 8], [868, 17], [870, 17], [871, 18], [872, 18], [873, 18], [874, 18], [879, 18], [880, 18], [881, 18], [890, 24], [891, 24], [892, 24], [893, 24], [894, 2], [895, 2], [896, 2], [897, 2], [898, 2], [899, 2], [900, 2], [901, 2], [902, 2], [903, 3], [904, 3], [905, 3], [906, 3], [907, 3], [908, 3], [909, 5], [910, 5], [911, 5], [912, 5], [913, 8], [914, 8], [915, 8], [916, 8], [917, 17], [918, 17], [919, 17], [920, 18], [921, 18], [922, 18], [923, 18], [929, 18], [939, 24], [940, 24], [941, 24], [942, 24], [943, 2], [944, 2], [945, 2], [946, 2], [947, 2], [948, 2], [949, 2], [950, 2], [951, 2], [952, 3], [953, 3], [954, 3], [955, 3], [956, 3], [957, 5], [958, 5], [959, 5], [960, 5], [961, 5], [962, 5], [963, 8], [964, 8], [965, 17], [966, 17], [967, 17], [968, 17], [989, 2], [990, 2], [991, 2], [992, 2], [993, 2], [994, 2], [995, 2], [996, 11], [997, 11], [998, 11], [999, 2], [1000, 2], [1001, 3], [1002, 3], [1003, 3], [1004, 3], [1005, 3], [1006, 9], [1007, 9], [1008, 9], [1009, 5], [1010, 5], [1011, 5], [1012, 8], [1013, 17], [1014, 17], [1015, 17], [1016, 17], [1017, 17], [1039, 26], [1040, 26], [1041, 2], [1042, 2], [1043, 2], [1044, 11], [1045, 11], [1046, 11], [1047, 2], [1048, 2], [1049, 3], [1050, 3], [1051, 3], [1052, 3], [1053, 3], [1054, 19], [1055, 9], [1056, 9], [1057, 1], [1058, 1], [1059, 17], [1060, 5], [1061, 17], [1062, 17], [1063, 17], [1064, 17], [1065, 17], [1066, 17], [1089, 26], [1090, 26], [1091, 2], [1092, 2], [1093, 2], [1094, 11], [1095, 11], [1096, 2], [1097, 11], [1098, 19], [1099, 19], [1100, 19], [1101, 19], [1102, 3], [1103, 19], [1104, 1], [1105, 1], [1106, 1], [1107, 1], [1108, 1], [1109, 1], [1110, 17], [1111, 17], [1112, 17], [1113, 15], [1114, 16], [1115, 17], [1116, 17], [1137, 26], [1138, 26], [1139, 26], [1140, 26], [1141, 26], [1142, 26], [1143, 26], [1144, 11], [1145, 11], [1146, 13], [1147, 11], [1148, 11], [1149, 19], [1150, 19], [1151, 19], [1152, 19], [1153, 1], [1154, 1], [1155, 1], [1156, 1], [1157, 1], [1158, 1], [1159, 17], [1160, 17], [1161, 17], [1162, 15], [1163, 16], [1164, 16], [1165, 17], [1186, 26], [1187, 26], [1188, 26], [1189, 26], [1190, 26], [1191, 11], [1192, 13], [1193, 11], [1194, 13], [1195, 13], [1196, 13], [1197, 11], [1198, 19], [1199, 19], [1200, 19], [1201, 19], [1202, 1], [1203, 1], [1204, 1], [1205, 1], [1206, 1], [1207, 20], [1208, 17], [1209, 17], [1210, 17], [1211, 17], [1212, 15], [1213, 15], [1214, 17], [1215, 17], [1236, 26], [1237, 26], [1238, 26], [1240, 11], [1241, 11], [1242, 13], [1243, 11], [1244, 13], [1245, 13], [1246, 19], [1247, 19], [1248, 19], [1249, 19], [1250, 19], [1251, 1], [1252, 1], [1253, 1], [1254, 1], [1255, 1], [1256, 20], [1257, 17], [1258, 17], [1259, 17], [1260, 17], [1261, 17], [1262, 17], [1263, 17], [1264, 17], [1290, 13], [1291, 12], [1292, 13], [1293, 19], [1294, 19], [1295, 19], [1296, 19], [1297, 19], [1298, 19], [1299, 19], [1300, 1], [1301, 1], [1302, 1], [1303, 1], [1304, 1], [1305, 20], [1306, 20], [1307, 20], [1308, 20], [1309, 20], [1310, 20], [1340, 12], [1341, 12], [1346, 19], [1347, 19], [1350, 1], [1351, 1], [1352, 1], [1353, 20], [1354, 20], [1355, 20], [1356, 20], [1357, 20], [1358, 20], [1398, 14], [1399, 14], [1400, 1], [1401, 20], [1402, 20], [1403, 20], [1404, 20], [1405, 20], [1406, 20], [1447, 14], [1448, 14], [1449, 14], [1450, 20], [1451, 20], [1497, 14]]





pathToGeoDictionary = r'Q:\\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\04-finalCH\dictionaryGEO.txt'
pathToAreTypologieDictionary = r'Q:\\Abteilungsprojekte\eng\SWWData\Eggimann_Sven\07-Fallbeispiele\04-finalCH\LOOKUPAREGEMTYP_DICTIONARY.txt'
pathResults = "GIS_PYTHON\\"

EW_Q = 0.162    # NEEDS OT BE THE SAME asin all other files

# Classification criteriat for WWTP SIZE
sizeSmallWWTP = 20        # Size in PE of Small treatment package plant        # CREABETON 4 - 30
sizeMiddleWWTP = 200      # Size in PE of Middle treatment package plant

pythonScriptPath = "C://Users/eggimasv/URBANDENSITY/P4/"    # Path to Python SNIP Files
sys.path.append(pythonScriptPath)                           # Append paths

# Import Geo of all Catchements ([BFS_NUMMER, KANTONSNUM, NAME, ARA_Nr, ARA_Name])
catchmentDictionaryNotSorted = readInGeoDictionary(pathToGeoDictionary)
print("LnethcatchmentDictionaryNotSorted: " + str(len(catchmentDictionaryNotSorted)))

# Get one community for each catchement which is in the dominant canton
#catchmentDictionary = assignCatchementsToCanton(catchmentDictionaryNotSorted, kantonGeoBFS)
#print("Number of catchements: " + str(len(catchmentDictionary)))

catchmentDictionary = catchmentDictionaryNotSorted

# CAN BE USED FOR ARA
areTypologie = readInARETypologieDictionary(pathToAreTypologieDictionary) #TYP, NAME, KT_NO, BFS_N

# Read out all Folders
ListWithWWTPCatchments = collectDataAllRuns(pathResultFolder)

# STistics per Canton [ARA_NR, kantonNr, gemeindeNr, Z, Z_weighted, percentageSmallWWTP, percentageMiddle, percentageLarge] #GEMEINDENR?
statisticsPerCatchement = []        

print("ListWithWWTPCatchments:" + str(len(ListWithWWTPCatchments)))
#prnt("..")

#TODO Create graph with percentages for all catchements (and not aggregated wiht Cantons)

# Iterate Folder
counter = 0
for pathCatchement in ListWithWWTPCatchments: 
    #print("--------------------")
    print("Path Catchement : " + str(pathCatchement))
    counter +=1 
    
    getNR = pathCatchement.split(FolderPath) #"CALCULATION_P4_CH_NEU")
    ARA_NR = int(getNR[1][1:])
       
    # Iterate all SNIP Calculations
    folderListSNIPResults= get_immediate_subdirectories(pathCatchement)
    
    # Read in Densities
    # ----------------
    pathExtent_gem = pathCatchement + "\\" + "extent_gem.shp"
    pathBuildings_inhabited = pathCatchement + "\\" + "buildings_inhabited.shp"
    pathSettArea =pathCatchement + "\\" + "settlementArea.shp"
    
    #print("pathExtent_gem: " + str(pathExtent_gem))
    #print("pathBuildings_inhabited: " + str(pathBuildings_inhabited))
    #print("pathSettArea: " + str(pathSettArea))
    
    regularpopDensity, NeighborhoodDensity, totCatchmentArea, totPopCatchement, totSettlmentAreaCatchement = getDensitiesCatchement(pathExtent_gem, pathBuildings_inhabited, pathSettArea, FISHNET)
    
    # ---------------------
    # Iterate SNIP Folders (mainly to get standard deviation)
    # ---------------------
    calc_SNIPs = [] # List for all calculations
    
    for SNIPcalculation in folderListSNIPResults:
        SNIPFolder = SNIPcalculation[len(SNIPcalculation)-8:]
            
        # Path to WWTPs text file with results
        pathFolderWWWTPResults = pathCatchement + "\\" + SNIPFolder
        #print("pathFolderWWWTPResults: " + str(pathFolderWWWTPResults))
        
        slopeCriteria = float(SNIPFolder[5] + SNIPFolder[7])
        #print("slopeCriteria: "+ str(slopeCriteria))
    
        # All .txt Files
        allFilesInFolder = glob.glob(pathFolderWWWTPResults + "\\" +  "*.txt")
        
        #print("allFilesInFolder: " + str(allFilesInFolder))
        pathstatisticsSNIP = allFilesInFolder[0] # Statistic File
        #print("pathstatisticsSNIP: " + str(pathstatisticsSNIP))
        
        statisticsSNIP_Slope = readStatistics(pathstatisticsSNIP)
        
        # Degress of Centralisation
        Z_SNIP = statisticsSNIP_Slope[3]
        Z_weighted_SNIP = statisticsSNIP_Slope[4]
        
        # Get WWTP statistics
        wwtpFile_SNIP = allFilesInFolder[11]
        WWTPS_SNIP = readInWWTPs(wwtpFile_SNIP)      
        
        # Calculate Populations
        totalPE_SNIP, percentageSmallWWTP_SNIP, percentageMiddle_SNIP, percentageLarge_SNIP = getPercentagesWWTP(WWTPS_SNIP, EW_Q, sizeSmallWWTP, sizeMiddleWWTP)
        
        # Append Results
        resultsIter = [slopeCriteria, Z_SNIP, Z_weighted_SNIP, percentageSmallWWTP_SNIP, percentageMiddle_SNIP, percentageLarge_SNIP]

        calc_SNIPs.append(resultsIter)
        
        # Restuls for the three scenario runs
        if SNIPcalculation == "SNIP_1_0":
            slopeCriteria_standardScenario = slopeCriteria
            Z_SNIP_standardScenario = Z_SNIP
            Z_weighted_SNIP_standardScenario = Z_weighted_SNIP
            percentageSmallWWTP_SNIP_standardScenario = percentageSmallWWTP_SNIP
            percentageMiddle_SNIP_standardScenario = percentageMiddle_SNIP
            percentageLarge_SNIP_standardScenario = percentageLarge_SNIP
        
        if SNIPcalculation == "SNIP_0_5":
            slopeCriteria_scenario05 = slopeCriteria
            Z_SNIP_scenario05 = Z_SNIP
            Z_weighted_SNIP_scenario05 = Z_weighted_SNIP
            percentageSmallWWTP_SNIP_scenario05 = percentageSmallWWTP_SNIP
            percentageMiddle_SNIP_scenario05 = percentageMiddle_SNIP
            percentageLarge_SNIP_scenario05 = percentageLarge_SNIP
        
        if SNIPcalculation == "SNIP_1_5":
            slopeCriteria_scenario15 = slopeCriteria
            Z_SNIP_scenario15 = Z_SNIP
            Z_weighted_SNIP_scenario15 = Z_weighted_SNIP
            percentageSmallWWTP_SNIP_scenario15 = percentageSmallWWTP_SNIP
            percentageMiddle_SNIP_scenario15 = percentageMiddle_SNIP
            percentageLarge_SNIP_scenario15 = percentageLarge_SNIP

    '''print("Iteratet Result Files")
    #print(calc_SNIPs)
    for i in calc_SNIPs:
        print i
    '''
    # Calculate Standard Deviation of three scenarios (for three scenario) for each catchement   
    stdv_Z_SNIP = numpy.std([calc_SNIPs[0][1], calc_SNIPs[1][1], calc_SNIPs[2][1]])
    stdv_Z_weighted_SNIP = numpy.std([calc_SNIPs[0][2], calc_SNIPs[1][2], calc_SNIPs[2][2]])
    stdv_percentageSmallWWTP_SNIP = numpy.std([calc_SNIPs[0][3], calc_SNIPs[1][3], calc_SNIPs[2][3]])
    stdv_percentageMiddle_SNIP = numpy.std([calc_SNIPs[0][4], calc_SNIPs[1][4], calc_SNIPs[2][4]])
    stdv_percentageLarge_SNIP = numpy.std([calc_SNIPs[0][5], calc_SNIPs[1][5], calc_SNIPs[2][5]])
    
    '''print("---------------------------------")
    print("Restuls for catchemetn Nr: " + str(ARA_NR))
    print("---------------------------------")
    print("stdv_Z_SNIP: " + str(stdv_Z_SNIP))
    print("stdv_Z_weighted_SNIP: " + str(stdv_Z_weighted_SNIP))
    print("stdv_percentageSmallWWTP_SNIP: " + str(stdv_percentageSmallWWTP_SNIP))
    print("stdv_percentageMiddle_SNIP: " + str(stdv_percentageMiddle_SNIP))
    print("stdv_percentageLarge_SNIP: " + str(stdv_percentageLarge_SNIP))
    ''' 
    # Find Geography in Dictionary
    for i in catchmentDictionary:
        
        # if fishnet --> Get Canton of fishnet ID
        # --------------------------------------
        if FISHNET == True:
            fishnetID = ARA_NR            
            for fishnet in dictionaryFishNet: #FISHID, KT_ID
                
                if fishnet[0] == ARA_NR:
                    fishKT = fishnet[1]
                    
                    for kt in kantonGeoBFS:
                        if kt[0] == fishKT:
                            ktLabel = kt[2]
                            break
                    
            if True == True:
                print("ARA_NR: " + str(ARA_NR))
                
                # Adds for every community the statistics for the whole catchement
                #gemeindeNr, kantonNr =  i[0], i[1]
                gemeindeNr, kantonNr =  0.00, fishKT 
                    
                statCatchement = [
                        
                        # Infos
                        ARA_NR, 
                        kantonNr, 
                        ktLabel, 
                        gemeindeNr, 
                        regularpopDensity, 
                        NeighborhoodDensity, 
                        totCatchmentArea, 
                        totPopCatchement, 
                        totSettlmentAreaCatchement, 
                        
                        # Standard Scenario
                        slopeCriteria_standardScenario,          
                        Z_SNIP_standardScenario, 
                        Z_weighted_SNIP_standardScenario, 
                        percentageSmallWWTP_SNIP_standardScenario, 
                        percentageMiddle_SNIP_standardScenario, 
                        percentageLarge_SNIP_standardScenario, 
                        
                        # Slope 0.5 Scenario
                        slopeCriteria_scenario05,
                        Z_SNIP_scenario05,
                        Z_weighted_SNIP_scenario05,
                        percentageSmallWWTP_SNIP_scenario05,
                        percentageMiddle_SNIP_scenario05,
                        percentageLarge_SNIP_scenario05,
                        
                        # Slope 1.5 Scenario
                        slopeCriteria_scenario15,
                        Z_SNIP_scenario15,
                        Z_weighted_SNIP_scenario15,
                        percentageSmallWWTP_SNIP_scenario15,
                        percentageMiddle_SNIP_scenario15,
                        percentageLarge_SNIP_scenario15,
                
                        # Std Deviation for individual catchements
                        stdv_Z_SNIP, 
                        stdv_Z_weighted_SNIP, 
                        stdv_percentageSmallWWTP_SNIP, 
                        stdv_percentageMiddle_SNIP, 
                        stdv_percentageLarge_SNIP
                        ]
                
                print("statCatchement: " + str(statCatchement))        
                # Append Statistics to canton
                statisticsPerCatchement.append(statCatchement)
                break        
                    
  
            
        
        else:#print("FLOL: " + str(i))
            #print("ARA_NR: " + str(ARA_NR))
            #if i[3] == ARA_NR:
            if i[1] == ARA_NR:
                print("ARA_NR: " + str(ARA_NR))
                
                # Adds for every community the statistics for the whole catchement
                #gemeindeNr, kantonNr =  i[0], i[1]
                gemeindeNr, kantonNr =  0.00, i[0] 
                    
    
                for kt in kantonGeoBFS:
                    if kt[0] == kantonNr:
                        ktLabel = kt[2]
                        break
                        
                statCatchement = [
                        
                        # Infos
                        ARA_NR, 
                        kantonNr, 
                        ktLabel, 
                        gemeindeNr, 
                        regularpopDensity, 
                        NeighborhoodDensity, 
                        totCatchmentArea, 
                        totPopCatchement, 
                        totSettlmentAreaCatchement, 
                        
                        # Standard Scenario
                        slopeCriteria_standardScenario,          
                        Z_SNIP_standardScenario, 
                        Z_weighted_SNIP_standardScenario, 
                        percentageSmallWWTP_SNIP_standardScenario, 
                        percentageMiddle_SNIP_standardScenario, 
                        percentageLarge_SNIP_standardScenario, 
                        
                        # Slope 0.5 Scenario
                        slopeCriteria_scenario05,
                        Z_SNIP_scenario05,
                        Z_weighted_SNIP_scenario05,
                        percentageSmallWWTP_SNIP_scenario05,
                        percentageMiddle_SNIP_scenario05,
                        percentageLarge_SNIP_scenario05,
                        
                        # Slope 1.5 Scenario
                        slopeCriteria_scenario15,
                        Z_SNIP_scenario15,
                        Z_weighted_SNIP_scenario15,
                        percentageSmallWWTP_SNIP_scenario15,
                        percentageMiddle_SNIP_scenario15,
                        percentageLarge_SNIP_scenario15,
                
                        # Std Deviation for individual catchements
                        stdv_Z_SNIP, 
                        stdv_Z_weighted_SNIP, 
                        stdv_percentageSmallWWTP_SNIP, 
                        stdv_percentageMiddle_SNIP, 
                        stdv_percentageLarge_SNIP
                        ]
                
                print("statCatchement: " + str(statCatchement))        
                # Append Statistics to canton
                statisticsPerCatchement.append(statCatchement)
                break
    #prnt("..")

print("-----------------------------------------------------------")
print("Number of catchements read in: " + str(len(statisticsPerCatchement)))
print("-----------------------------------------------------------")

print"FINISHED"
for i in statisticsPerCatchement:
    print(i)
    #print"----------"
#prnt("..")


# ---------------------------------------------------------------------------
# Create Graphs
# ---------------------------------------------------------------------------
from P4_barcharts import *
from P4_figureDensityCatchement import *

# PLot Figure with all WWTPs
print(" Print all catchements of a canton")
#plotAllCatchements(statisticsPerCatchement, ['ZH'])

# Plot Figure with Cnatons and percetnages 
#plotFigureCantons3Classes(statisticsPerCatchement)


# PLot Densitiey and percentage for catchements
print(" Print all densities")
figureRetularDensityCatchement(statisticsPerCatchement)
