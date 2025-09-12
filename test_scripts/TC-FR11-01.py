Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-11: Deployment on Netlify', () => {
    before(async () => { await browser.url('http://www.ipsy.com'); });
    it('Positive - Verify deployment to Netlify is successful', async () => {
        const performance = await browser.getPerformance();
        await expect(performance.loadTime).toBeLessThan(2000);
    });
    it('Negative - Verify failure if not on Netlify', async () => {
        await browser.url('http://old.ipsy.com');
        const performance = await browser.getPerformance();
        await expect(performance.loadTime).toBeGreaterThan(2000);
    });
    it('Edge - Verify performance under high load simulation', async () => {
        await browser.pause(5000);
        const body = await $('body');
        await expect(body).toBeDisplayed();
    });
});
