// Optional browser validation. Requires Playwright and Chromium; not needed for replay.
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
 const root=path.resolve(__dirname,'../../..');
 if(!process.argv[2])throw new Error('Supply a fresh local core run directory; shipped outputs are read-only');
 const out=fs.realpathSync(path.resolve(process.argv[2]));
 const relative=path.relative(root,out);
 if(relative===''||(!relative.startsWith('..'+path.sep)&&!path.isAbsolute(relative)&&relative.split(path.sep)[0]!=='runs'))throw new Error('Shipped checkout files are read-only; use runs/ or an external local directory');
 for(const name of ['preview-desktop.png','preview-mobile.png'])if(fs.existsSync(path.join(out,name)))throw new Error('Screenshots already exist; use a fresh local run');
 const {chromium}=require('playwright');

 const ir=JSON.parse(fs.readFileSync(path.join(out,'ir.json'),'utf8'));
 const browser=await chromium.launch({...(process.env.CHROMIUM_EXECUTABLE_PATH?{executablePath:process.env.CHROMIUM_EXECUTABLE_PATH}:fs.existsSync('/usr/bin/chromium')?{executablePath:'/usr/bin/chromium'}:{}),headless:true,args:['--no-sandbox']});
 let page=await browser.newPage({viewport:{width:1280,height:1000}});const errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.setContent(fs.readFileSync(path.join(out,'advisor-explorer.html'),'utf8'));
 const base=await page.evaluate(()=>model(data.config.scenarios[0],cv('avg_net_unit_sf'),cv('hard_cost_per_gsf'),cv('annual_interest')*100,cv('monthly_rent_test')));
 const p='scenario.'+ir.lead_decision.bbl+'.A.';
 for(const [jsKey,irKey] of [['gross','gross_sf'],['units','units'],['floors','floors'],['total','ex_land_cost'],['need','debt_support_rent_month'],['extra','additional_non_debt_capital']]){
  assert(Math.abs(base[jsKey]-ir.claims[p+irKey].value)<0.00001,'Browser calculation mismatch '+jsKey);
 }
 await page.screenshot({path:path.join(out,'preview-desktop.png')});
 await page.locator('#unitsize').fill('1000');await page.locator('#unitsize').dispatchEvent('input');
 const changed=await page.locator('#metrics').innerText();assert(changed.includes('230'),'Changed home-size assumption did not propagate');
 await page.locator('#reset').click();assert((await page.locator('#metrics').innerText()).includes('271'),'Reset failed');
 await page.locator('#trace-cost').click();assert((await page.locator('#trace').innerText()).includes('assumption.hard_cost_per_gsf'),'Trace dependency missing');
 const points=await page.locator('svg').first().locator('g circle').evaluateAll(nodes=>nodes.map(n=>({x:+n.getAttribute('cx'),y:+n.getAttribute('cy')})));
 assert(points.length===10&&points.every(p=>p.x>10&&p.x<590&&p.y>10&&p.y<590),'Map points clipped');
 await page.close();page=await browser.newPage({viewport:{width:390,height:844}});page.on('pageerror',e=>errors.push(e.message));await page.setContent(fs.readFileSync(path.join(out,'advisor-explorer.html'),'utf8'));
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
 assert(!overflow,'Mobile document overflows');
 await page.screenshot({path:path.join(out,'preview-mobile.png')});
 assert.deepStrictEqual(errors,[],'Browser errors');
 console.log(JSON.stringify({status:'passed',formula_parity:true,sliders:true,reset:true,claim_trace:true,mobile_overflow:false,page_errors:errors}));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
